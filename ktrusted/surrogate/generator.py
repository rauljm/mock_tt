from pyspark.sql import functions as f


def surrogate(*cols):
    def run():
        any_is_null = None
        for col in cols:
            col_is_null = f.isnull(f.col(col))
            any_is_null = col_is_null if any_is_null is None else (any_is_null | col_is_null)

        col_sk = (
            f.when(any_is_null, '-1')
            .otherwise(
                f.md5(f.concat_ws('-', *cols)))
            .cast('string'))

        return col_sk

    return run
