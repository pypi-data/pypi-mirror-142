import logging

import dateparser
import pandas as pd
from pandas import DataFrame

log = logging.getLogger(__name__)


def ingest_timeseries(param_config: dict):
    """Retrieve the time-series data at the URL specified in `param_config['input parameters']` and return it in a
    Pandas' DataFrame.
    This can be used for the initial data ingestion, i.e. to ingest the initial time-series which will be clustered.

    Parameters
    ----------
    param_config : dict
        A dictionary corresponding to a TIMEX JSON configuration file.

    Returns
    -------
    df_ingestion : DataFrame
        Pandas DataFrame corresponding to the CSV files specified in param_config, with the various pre-processing steps
        applied. In particular, a frequency has been forced to the datetime index, NaN values have been interpolated.

    Notes
    -----
    In particular, the `input_parameters` sub-dictionary part of `param_config` will be used. In `input_parameters`, the
    following options has to be specified:

    - `source_data_url`: local or remote URL pointing to a CSV file;

    Additionally, some other parameters can be specified:

    - `index_column_name`: the name of the column to use as index for the DataFrame. If not specified the first one will
      be used. This column's values will be parsed with dateparser to obtain a DateTimeIndex;
    - `frequency`: if specified, the corresponding frequency will be imposed. Refer to
      https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases for a list of possible
      values. If not specified the frequency will be infered.
    - `columns_to_load_from_url`: comma-separated string of columns' names which will be read from the CSV file. If not
      specified, all columns will be read;
    - `timeseries_names`: dictionary of key-values (old_name: new_name) used to rename some columns in the CSV;
    - `dateparser_options`: dictionary of key-values which will be given to `dateparser.parse()`.

    Examples
    --------
    >>> timex_dict = {
    ...  "input_parameters": {
    ...    "source_data_url": "https://raw.githubusercontent.com/uGR17/TIMEX_CLUSTERING/main/examples/datasets/k_means_example_5ts.csv",
    ...    "columns_to_load_from_url": "date,ts1,ts2,ts3,ts4,ts5,ts6,ts7,ts8,ts9,ts10,ts11,ts12",
    ...    "index_column_name": "date",
    ...    "frequency": "D",  
    ...    "timeseries_names": {
    ...        "date": "Data",
    ...        "ts1": "time_series1",
    ...        "ts2": "time_series2",
    ...    }
    ...  }
    ...}
    >>> ingest_timeseries(timex_dict)
            time_series1	time_series2	ts3	ts4	ts5	ts6	ts7	ts8	ts9	ts10	ts11	ts12
    Data												
    2020-01-03	0.718000	0.805000	-1.490000	0.732000	-2.030000	0.726000	0.587000	0.600000	0.6970	-1.3800	-1.660000	-1.590000
    2020-01-04	0.537000	0.706000	0.726000	0.692000	0.582000	0.656000	0.522000	0.593000	0.5620	0.7920	0.623000	0.725000
    ...	...	...	...	...	...	...	...	...	...	...	...	...
    2020-12-02	-1.147667	-1.166667	0.671433	-2.011667	0.526933	-2.052333	-1.920333	-1.613000	-1.7320	0.6178	0.692367	0.672567
    2020-12-03	-1.240000	-1.160000	0.673000	-2.010000	0.527000	-2.050000	-1.920000	-1.610000	-1.7300	0.6280	0.694000	0.674000
    [336 rows × 12 columns]
    """
    
    log.info('Starting the data ingestion phase.')
    input_parameters = param_config["input_parameters"]

    source_data_url = input_parameters['source_data_url']

    try:
        columns_to_load_from_url = input_parameters["columns_to_load_from_url"]
        columns_to_read = list(columns_to_load_from_url.split(','))
        # We append [columns_to_read] to read_csv to maintain the same order of columns also in the df.
        df_ingestion = pd.read_csv(source_data_url, usecols=columns_to_read)[columns_to_read]

    except (KeyError, ValueError):
        df_ingestion = pd.read_csv(source_data_url)

    try:
        index_column_name = input_parameters["index_column_name"]
    except KeyError:
        index_column_name = df_ingestion.columns[0]

    log.debug(f"Parsing {index_column_name} as datetime column...")

    dateparser_options = {
        "settings": {
            "PREFER_DAY_OF_MONTH": "first"
        }
    }

    if "dateparser_options" in input_parameters:
        dateparser_options = input_parameters["dateparser_options"]
        df_ingestion[index_column_name] = df_ingestion[index_column_name].apply(
            lambda x: dateparser.parse(x, **dateparser_options)
        )
    else:
        df_ingestion[index_column_name] = df_ingestion[index_column_name].apply(
            lambda x: dateparser.parse(x)
        )

    df_ingestion.set_index(index_column_name, inplace=True, drop=True)

    log.debug(f"Removing duplicates rows from dataframe; keep the last...")
    df_ingestion = df_ingestion[~df_ingestion.index.duplicated(keep='last')]

    if not df_ingestion.index.is_monotonic_increasing:
        log.warning(f"Dataframe is not ordered. Ordering it...")
        df_ingestion = df_ingestion.sort_index()
        
    try:
        mappings = input_parameters["timeseries_names"]
        df_ingestion.reset_index(inplace=True)
        df_ingestion.rename(columns=mappings, inplace=True)
        try:
            df_ingestion.set_index(mappings.get(index_column_name), inplace=True)
        except KeyError:
            df_ingestion.set_index(index_column_name, inplace=True)
    except KeyError:
        pass

    try:
        freq = input_parameters["frequency"]
    except KeyError:
        freq = None

    df_ingestion = add_freq(df_ingestion, freq)
    df_ingestion = df_ingestion.interpolate()

    log.info(f"Finished the data-ingestion phase. Some stats:\n"
             f"-> Number of rows: {len(df_ingestion)}\n"
             f"-> Number of columns: {len(df_ingestion.columns)}\n"
             f"-> Column names: {[*df_ingestion.columns]}\n"
             f"-> Number of missing data: {[*df_ingestion.isnull().sum()]}")

    return df_ingestion


def add_freq(df, freq=None) -> DataFrame:
    """Add a frequency to the index of df. Pandas DatetimeIndex have a `frequency` attribute; this function tries to
    assign a value to that attribute.

    If the index of df is a DatetimeIndex, then this function is guaranteed to return a DataFrame with the `frequency`
    attribute set. If it is not possible to assign the frequency, datetime may be normalized (i.e. keep only the date
    part and remove hour) in order to obtain days.

    Parameters
    ----------
    df : DataFrame
        Pandas DataFrame on which a frequency will be added.

    freq : str, optional
        If this attribute is specified, then the corresponding frequency will be forced on the DataFrame. If it is not
        specified, than, the frequency will be estimated.
        `freq` should be a so called 'offset alias'; the possible values can be found at
        https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases

    Returns
    -------
    local_df : DataFrame
        df with the DatetimeIndex.freq set; if df did not have a DatetimeIndex, then df is returned unmodified.

    Examples
    --------
    >>> dates = [pd.Timestamp(datetime(year=2020, month=1, day=1, hour=10, minute=00)),
    ...          pd.Timestamp(datetime(year=2020, month=1, day=2, hour=12, minute=21)),
    ...          pd.Timestamp(datetime(year=2020, month=1, day=3, hour=13, minute=30)),
    ...          pd.Timestamp(datetime(year=2020, month=1, day=4, hour=11, minute=32))]
    >>> df = pd.DataFrame(data={"a": [0, 1, 2, 3]}, index=dates)
    >>> df
                         a
    2020-01-01 10:00:00  0
    2020-01-02 12:21:00  1
    2020-01-03 13:30:00  2
    2020-01-04 11:32:00  3

    `df` does not have a fixed frequency in its DatetimeIndex:

    >>> df.index.freq
    None

    Try to apply it:

    >>> df_with_freq = add_freq(df)
    >>> df_with_freq
                a
    2020-01-01  0
    2020-01-02  1
    2020-01-03  2
    2020-01-04  3

    Hours have been removed. Check the frequency of the index:

    >>> df_with_freq.index.freq
    <Day>
    """
    local_df = df.copy()

    # Check if df has a DatetimeIndex. If not, return without doing anything.
    try:
        i = local_df.index.freq
    except:
        return local_df

    # Df has already a freq. Don't do anything.
    if local_df.index.freq is not None:
        return local_df

    if freq is not None:
        if freq == 'D':
            local_df.index = local_df.index.normalize()

        local_df = local_df.asfreq(freq=freq)
        return local_df

    if freq is None:
        freq = pd.infer_freq(local_df.index)

        if freq is None:
            local_df.index = local_df.index.normalize()
            freq = pd.infer_freq(local_df.index)

        if freq is None:
            log.warning(f"No discernible frequency found for the dataframe.")
            freq = "D"

        local_df = local_df.asfreq(freq=freq)
        return local_df


def select_timeseries_portion(data_frame, param_config):
    """This allows the user to select only a part of a time-series DataFrame, according to some criteria (e.g. date).

    Parameters
    ----------
    data_frame : DataFrame
        Pandas DataFrame from which select a portion.
    param_config : dict
        A dictionary corresponding to a TIMEX JSON configuration file.

    Returns
    -------
    df: DataFrame
        Pandas' DataFrame after the selection phase.

    Notes
    -----
    In particular, the selection_parameters sub-dictionary part of param_config will be used. In selection_parameters,
    the following options can to be specified:

    - column_name_selection: if specified, only the rows in which the value of the column named `column_name_selection`
    is equal to `value_selection` are kept. If this is specified, also `value_selection` has to be specified.
    - init_datetime: if specified, only the rows where the Datetimeindex value is greater than `init_datetime` are kept.
    - end_datetime: if specified, only the rows where the Datetimeindex value is less than `end_datetime` are kept.

    Moreover, if `dateparser_options` is specified in `param_dict[input_parameters]', then the options will be passed to
    dateparser to parse the dates.

    Examples
    --------
    >>> ds = pd.date_range('2000-01-01', periods=7)
    >>> a = numpy.arange(30, 37)
    >>> b = numpy.array([0, 0, 0, 1, 1, 1, 0])
    >>> df = DataFrame(data={"a": a, "b": b}, index=ds)
    >>> print(df)
                 a  b
    2000-01-01  30  0
    2000-01-02  31  0
    2000-01-03  32  0
    2000-01-04  33  1
    2000-01-05  34  1
    2000-01-06  35  1
    2000-01-07  36  0

    Select using an initial time and an end time:

    >>> timex_config = {
    ...   "selection_parameters" : {
    ...     "init_datetime": '2000-01-02',
    ...     "end_datetime": '2000-01-05'
    ...   }
    ...}
    >>> selected_df = select_timeseries_portion(df, timex_config)
                 a  b
    2000-01-02  31  0
    2000-01-03  32  0
    2000-01-04  33  1
    2000-01-05  34  1

    Select using the value for a column:

    >>> timex_config = {
    ...   "selection_parameters" : {
    ...    "column_name_selection": "b",
    ...    "value_selection": 1
    ...   }
    ...}
    >>> selected_df = select_timeseries_portion(df, timex_config)
                 a  b
    2000-01-04  33  1
    2000-01-05  34  1
    2000-01-06  35  1
    """
    try:
        selection_parameters = param_config["selection_parameters"]
    except KeyError:
        log.debug(f"Selection phase not requested by user. Skip.")
        return data_frame

    try:
        input_parameters = param_config['input_parameters']
    except KeyError:
        input_parameters = {}

    log.info(f"Total amount of rows before the selection phase: {len(data_frame)}")

    if "column_name_selection" in selection_parameters and "value_selection" in selection_parameters:
        column_name = param_config['selection_parameters']['column_name_selection']
        value = param_config['selection_parameters']['value_selection']

        log.debug(f"Selection over column {column_name} with value = {value}")
        data_frame = data_frame.loc[data_frame[column_name] == value]

    if "init_datetime" in selection_parameters:
        if "dateparser_options" in input_parameters:
            dateparser_options = input_parameters["dateparser_options"]
            init_datetime = dateparser.parse(selection_parameters['init_datetime'], **dateparser_options)
        else:
            init_datetime = dateparser.parse(selection_parameters['init_datetime'])

        log.debug(f"Selection over date, keep data after {init_datetime}")
        mask = (data_frame.index.to_series() >= init_datetime)
        data_frame = data_frame.loc[mask]

    if "end_datetime" in selection_parameters:
        if "dateparser_options" in input_parameters:
            dateparser_options = input_parameters["dateparser_options"]
            end_datetime = dateparser.parse(selection_parameters['end_datetime'], **dateparser_options)
        else:
            end_datetime = dateparser.parse(selection_parameters['end_datetime'])

        log.debug(f"Selection over date, keep data before {end_datetime}")
        mask = (data_frame.index.to_series() <= end_datetime)
        data_frame = data_frame.loc[mask]

    log.info(f"Total amount of rows after the selection phase: {len(data_frame)}")
    return data_frame
