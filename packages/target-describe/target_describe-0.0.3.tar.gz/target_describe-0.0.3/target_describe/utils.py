from typing import Optional
from typing_extensions import Literal
from unicodedata import category
import pandas as pd
import numpy as np
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def select_numeric(x: pd.DataFrame) -> pd.DataFrame:
    x = x.select_dtypes(include=[np.number], exclude=[bool])

    # print(x)
    return x


def select_categorical_text(x: pd.DataFrame) -> pd.DataFrame:
    x = x.select_dtypes(exclude=[np.number])
    """
    Select non numeric columns from a Dataframe

    Returns:
        pd.DataFrame: DataFrame with just categorical data
    """
    # print(x)
    return x


def calculate_distribution(
    df: pd.DataFrame, variable: str, target_name: str, target_value_described: str, sort_by: Literal["rows", "variable", "target_asc", "target_desc"]
) -> pd.DataFrame:

    df = get_variable_and_target(df, variable, target_name)

    dummy_names = [target_name + "_" +
                   str(dummy) for dummy in df[target_name].unique()]
    target_value_described = target_name + "_" + target_value_described
    df = pd.get_dummies(data=df, columns=[target_name])
    df = df.groupby(by=variable)[dummy_names].sum()
    df["Total"] = df.sum(axis=1).astype(int)
    df = df.astype(int).reset_index()
    df["Percentage"] = (df[target_value_described] / df["Total"]) * 100

    if sort_by == "rows":
        df.sort_values(by="Total", inplace=True, ascending=False)
    elif sort_by == "variable":
        df.sort_values(by=variable, inplace=True)

    elif sort_by == "target_asc":
        df.sort_values(by="Percentage", ascending=True, inplace=True)
    elif sort_by == "target_desc":
        df.sort_values(by="Percentage",
                       ascending=False, inplace=True)
    # x = (
    #     df[df[target_name] == df[target_name].unique()[-1]]
    #     .groupby(variable)[target_name]
    #     .count()
    # )
    # y = (
    #     df[df[target_name] == df[target_name].unique()[0]]
    #     .groupby(variable)[target_name]
    #     .count()
    # )

    # vv = pd.DataFrame({variable: df[variable].unique()})

    # vv = pd.merge(vv, x, how="left", right_index=True, left_on=variable)
    # vv = pd.merge(
    #     vv, y, how="left", right_index=True, left_on=variable, suffixes=("", "_not")
    # )
    # vv.fillna(0, inplace=True)
    # vv["Total"] = vv[target_name] + vv[target_name + "_not"]
    # vv["Percentage"] = (vv[target_name] / vv["Total"]) * 100

    return df


def sample_and_get_distribution(
    df: pd.DataFrame,
    variable: str,
    target_name: str,
    target_value_described: str,
    sample_size: int,
    random_state: Optional[int] = None,
) -> pd.DataFrame:
    df = get_variable_and_target(df, variable, target_name=target_name)
    dummy_names = [target_name + "_" +
                   str(dummy) for dummy in df[target_name].unique()]
    target_value_described = target_name + "_" + target_value_described
    df = pd.get_dummies(data=df, columns=[target_name])
    df = df.groupby(by=variable)[dummy_names].sum()

    if random_state:
        sample = df.sample(n=sample_size, random_state=random_state)
    else:
        sample = df.sample(n=sample_size)

    resto = df.drop(sample.index)
    resto = resto.sum()
    resto = pd.DataFrame(resto).T
    resto.index = ["All others"]

    df = pd.concat([sample, resto])
    df.index.name = variable

    df["Total"] = df.sum(axis=1).astype(int)
    df = df.astype(int).reset_index()
    df["Percentage"] = (df[target_value_described] / df["Total"]) * 100
    return df


def calculate_bins(
    df: pd.DataFrame,
    variable: str,
    target_name: str,
    target_value_described: str,
    nbins: int,
):
    df = get_variable_and_target(df, variable, target_name)
    dummy_names = [target_name + "_" +
                   str(dummy) for dummy in df[target_name].unique()]
    dummy_dct = {dummy_name: "sum" for dummy_name in dummy_names}
    target_value_described = target_name + "_" + target_value_described
    df = pd.get_dummies(data=df, columns=[target_name])
    df = df[df[variable].notna()]  # we ommit the na
    counts, bins = np.histogram(df[variable], bins=nbins)
    # bins = 0.5 * (bins[:-1] + bins[1:])
    df.loc[:, "Belong"] = np.digitize(df[variable], bins)
    df = df.groupby(by="Belong").agg({**{variable: "median"}, **dummy_dct})
    # df = df.reindex(list(range(df.index.min(), df.index.max() + 1)), fill_value=0)
    df["Total"] = df[dummy_names].sum(axis=1)
    df["Percentage"] = (df[target_value_described] / df["Total"]) * 100
    # df["Percentage"].fillna(0, inplace=True)
    return df, counts, bins


def get_variable_and_target(
    df: pd.DataFrame, variable_name: str, target_name: str
) -> pd.DataFrame:
    return df[[variable_name, target_name]]


def plot_variable(
    df: pd.DataFrame,
    variable_name: str,
    target_name: str,
    target_value_described: str,
    export: bool = False,
) -> None:

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=df[variable_name], y=df["Total"], marker_color="#1f77b4"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=df[variable_name],
            y=df["Percentage"],
            mode="markers",
            marker={"size": 20},
            marker_color="#fd3216",
        ),
        secondary_y=True,
    )

    fig.update_xaxes(title_text=f"{variable_name}", type="category")
    fig.update_yaxes(
        title_text="Number of rows",
        secondary_y=False,
        title_font=dict(color="#1f77b4"),
        color="#1f77b4",
    )
    fig.update_yaxes(
        title_text=f"Percentage of {target_name} = {target_value_described}",
        secondary_y=True,
        title_font=dict(color="#fd3216"),
        color="#fd3216",
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(categoryorder="array", categoryarray=df[variable_name])
    if export:
        fig.write_html(f"{variable_name+'_'+target_value_described}.html")

    if not export:
        # initiate notebook for offline plot
        init_notebook_mode(connected=True)
        iplot(fig)


def plot_numerical_variable(
    df: pd.DataFrame,
    grouped_bins: pd.DataFrame,
    counts,
    bins,
    variable_name: str,
    target_name: str,
    target_value_described: str,
    nbins: int,
    nbins_round_2: Optional[dict] = None,
    export: bool = False,
) -> None:

    size = np.ediff1d(bins)[0]
    min_hist = np.min(bins)
    max_hist = np.max(bins)

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # hist = px.histogram(df, x=variable_name, nbins=nbins)
    fig.add_trace(
        go.Histogram(
            x=df[variable_name],
            xbins={"start": min_hist, "size": size, "end": max_hist + 1},
            marker_color="#1f77b4",
        ),
        secondary_y=False,
    )
    # nbins = (
    # px.histogram(
    # df, x=variable_name, nbins=nbins, color_discrete_sequence=["#1f77b4"]
    # )
    # .full_figure_for_development()
    # .data[0]
    # .xbins["size"]
    # )

    # grouped_bins = calculate_bins(
    # df, variable_name, target_name, target_value_described, nbins
    # )

    # fig.add_trace(
    # go.Bar(x=bins, y=counts, marker_color="#1f77b4"), secondary_y=False,
    # )
    if nbins_round_2:
        if variable_name in nbins_round_2.keys():
            grouped_bins = calculate_bins(
                df,
                variable_name,
                target_name,
                target_value_described,
                nbins_round_2[variable_name] - 1,  # forsousky
            )

    fig.add_trace(
        go.Scatter(
            x=grouped_bins[variable_name],
            # x=bins,
            y=grouped_bins["Percentage"],
            mode="markers+lines",
            marker={"size": 20},
            marker_color="#fd3216",
        ),
        secondary_y=True,
    )

    fig.update_xaxes(title_text=f"{variable_name}")
    fig.update_yaxes(
        title_text="Number of rows",
        secondary_y=False,
        title_font=dict(color="#1f77b4"),
        color="#1f77b4",
    )
    fig.update_yaxes(
        title_text=f"Percentage of {target_name} = {target_value_described}",
        secondary_y=True,
        title_font=dict(color="#fd3216"),
        color="#fd3216",
    )
    fig.update_layout(showlegend=False)
    if export:
        fig.write_html(f"{variable_name+'_'+target_value_described}.html")
    if not export:
        # initiate notebook for offline plot
        init_notebook_mode(connected=True)
        iplot(fig)
