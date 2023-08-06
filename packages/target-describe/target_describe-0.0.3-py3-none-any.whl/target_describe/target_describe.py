from typing import List, Optional, Union
from typing_extensions import Literal
import pandas as pd
from .utils import (
    calculate_bins,
    get_variable_and_target,
    plot_numerical_variable,
    sample_and_get_distribution,
    select_categorical_text,
    select_numeric,
    plot_variable,
    calculate_distribution,
)


class targetDescribe:
    def __init__(
        self,
        data: pd.DataFrame,
        target: Union[pd.Series, str],
        problem: Literal["binary_classification", "regression"],
        max_categories: int = 30,
        target_described: Optional[str] = None,
        nbins: int = 15,
    ) -> None:
        __target_in_df = False

        if isinstance(target, str):
            try:
                self._target_name = target
                self.target = data[target].copy()
                __target_in_df = True
            except KeyError:
                raise KeyError(f"{target} not in DataFrame")
        else:
            self._target_name = target.name
            self.target = target.copy()

        if target_described:
            self.target_value_described = target_described
        else:
            self.target_value_described = str(self.target.unique()[-1])
        self.nbins = nbins
        self.max_categories = max_categories
        self.data = data.copy()
        self.problem = problem

        self.split_variables()
        self.numeric_variables = self._append_target(
            variables=self.numeric_variables, target_in_df=__target_in_df
        )
        self.categorical_variables = self._append_target(
            variables=self.categorical_variables, target_in_df=__target_in_df
        )

    def split_variables(self) -> None:
        self.numeric_variables = select_numeric(self.data)
        self.categorical_variables = select_categorical_text(self.data)

    def _append_target(
        self, variables: pd.DataFrame, target_in_df: bool
    ) -> pd.DataFrame:

        if target_in_df:
            if self.target.name in list(variables.columns):
                return variables
            else:
                return pd.concat([variables, self.target], axis=1)
        else:
            return pd.concat([variables, self.target], axis=1)

    def all_associations(
        self,
        target_value_described: Optional[str] = None,
        export: bool = False,
        max_categories: Optional[int] = None,
        nbins: Optional[int] = None,
        random_state: Optional[int] = None,
        nbins_round_2: Optional[dict] = None,
        sort_by: Literal["rows", "variable",
                         "target_asc", "target_desc"] = "rows"
    ):
        if nbins:
            self.nbins = nbins
        if max_categories:
            self.max_categories = max_categories

        if target_value_described:
            self.target_value_described = target_value_described
        if sort_by not in ["rows", "variable", "target_asc", "target_desc"]:
            print("Incorrect sort_by option using default")
            sort_by = "rows"

        if self.problem == "binary_classification":

            if self.target.nunique() != 2:
                raise ("Not binary target")

            numeric_columns = [
                name
                for name in list(self.numeric_variables.columns)
                if name not in [self._target_name]
            ]
            categorical_columns = [
                name
                for name in list(self.categorical_variables.columns)
                if name not in [self._target_name]
            ]

            for nombre in numeric_columns:
                if self.numeric_variables[nombre].dtype in ["int64", "int32", "int16"]:
                    num_categorias = self.numeric_variables[nombre].nunique()

                    if num_categorias <= self.max_categories:
                        proporcion = calculate_distribution(
                            df=self.numeric_variables,
                            variable=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            sort_by=sort_by
                        )

                        plot_variable(
                            df=proporcion,
                            variable_name=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            export=export,
                        )
                    else:

                        proporcion = sample_and_get_distribution(
                            df=self.numeric_variables,
                            variable=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            sample_size=self.max_categories,
                            random_state=random_state,
                        )

                        plot_variable(
                            df=proporcion,
                            variable_name=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            export=export,
                        )
                elif self.numeric_variables[nombre].dtype in ["float64", "float32"]:
                    proporcion, counts, bins = calculate_bins(
                        df=self.numeric_variables,
                        variable=nombre,
                        target_name=self._target_name,
                        target_value_described=self.target_value_described,
                        nbins=self.nbins,
                    )

                    plot_numerical_variable(
                        get_variable_and_target(
                            self.numeric_variables, nombre, self._target_name
                        ),
                        proporcion,
                        counts,
                        bins,
                        variable_name=nombre,
                        target_name=self._target_name,
                        target_value_described=self.target_value_described,
                        nbins=self.nbins,
                        nbins_round_2=nbins_round_2,
                        export=export,
                    )
            for nombre in categorical_columns:
                if self.categorical_variables[nombre].dtype == "object":
                    num_categorias = self.categorical_variables[nombre].nunique(
                    )
                    if num_categorias <= self.max_categories:

                        proporcion = calculate_distribution(
                            df=self.categorical_variables,
                            variable=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            sort_by=sort_by
                        )

                        plot_variable(
                            df=proporcion,
                            variable_name=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            export=export,
                        )

                    else:

                        proporcion = sample_and_get_distribution(
                            df=self.categorical_variables,
                            variable=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            sample_size=self.max_categories,
                            random_state=random_state,
                        )

                        plot_variable(
                            df=proporcion,
                            variable_name=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            export=export,
                        )

    def describe_some(self, columns: List[str], target_value_described: Optional[str] = None, export: bool = False, max_categories: Optional[int] = None, nbins: Optional[int] = None, random_state: Optional[int] = None, nbins_round_2: Optional[dict] = None, sort_by: Literal["rows", "variable", "target_asc", "target_desc"] = "rows"):
        if nbins:
            self.nbins = nbins
        if max_categories:
            self.max_categories = max_categories

        if target_value_described:
            self.target_value_described = target_value_described
        if sort_by not in ["rows", "variable", "target_asc", "target_desc"]:
            print("Incorrect sort_by option using default")
            sort_by = "rows"

        if self.problem == "binary_classification":
            if self.target.nunique() != 2:
                raise ("Not binary target")

            for nombre in columns:
                if nombre in self.numeric_variables.columns:

                    if self.numeric_variables[nombre].dtype in ["int64", "int32", "int16"]:
                        num_categorias = self.numeric_variables[nombre].nunique(
                        )

                        if num_categorias <= self.max_categories:
                            proporcion = calculate_distribution(
                                df=self.numeric_variables,
                                variable=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                sort_by=sort_by
                            )

                            plot_variable(
                                df=proporcion,
                                variable_name=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                export=export,
                            )
                        else:

                            proporcion = sample_and_get_distribution(
                                df=self.numeric_variables,
                                variable=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                sample_size=self.max_categories,
                                random_state=random_state,
                            )

                            plot_variable(
                                df=proporcion,
                                variable_name=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                export=export,
                            )
                    elif self.numeric_variables[nombre].dtype in ["float64", "float32"]:
                        proporcion, counts, bins = calculate_bins(
                            df=self.numeric_variables,
                            variable=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            nbins=self.nbins,
                        )

                        plot_numerical_variable(
                            get_variable_and_target(
                                self.numeric_variables, nombre, self._target_name
                            ),
                            proporcion,
                            counts,
                            bins,
                            variable_name=nombre,
                            target_name=self._target_name,
                            target_value_described=self.target_value_described,
                            nbins=self.nbins,
                            nbins_round_2=nbins_round_2,
                            export=export,
                        )

                elif nombre in self.categorical_variables.columns:

                    if self.categorical_variables[nombre].dtype == "object":
                        num_categorias = self.categorical_variables[nombre].nunique(
                        )
                        if num_categorias <= self.max_categories:

                            proporcion = calculate_distribution(
                                df=self.categorical_variables,
                                variable=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                sort_by=sort_by

                            )

                            plot_variable(
                                df=proporcion,
                                variable_name=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                export=export,
                            )

                        else:

                            proporcion = sample_and_get_distribution(
                                df=self.categorical_variables,
                                variable=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                sample_size=self.max_categories,
                                random_state=random_state,
                            )

                            plot_variable(
                                df=proporcion,
                                variable_name=nombre,
                                target_name=self._target_name,
                                target_value_described=self.target_value_described,
                                export=export,
                            )

                else:
                    print(f"{nombre} no esta en el dataframe cainal")


if __name__ == "__main__":

    df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    hola = df["Survived"].astype(str)
    df.drop(axis=1, labels="Survived", inplace=True)
    # print(df.columns)
    # a = targetDescribe(data=df, target="Survived", problem="binary_classification")

    b = targetDescribe(data=df, target=hola, problem="binary_classification")

    b.all_associations(
        max_categories=10, export=True,
    )
    # b.all_associations(export=True, target_value_described="0")
