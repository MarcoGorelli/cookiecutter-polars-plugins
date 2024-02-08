#![allow(clippy::unused_unit)]
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

fn impl_add_one<T>(ca: &ChunkedArray<T>) -> ChunkedArray<T>
where
    T: PolarsNumericType,
{
    ca.apply_values(|v: T::Native| v+1)
}

#[polars_expr(output_type_func=same_output_type)]
fn add_one(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let out = match s.dtype() {
        DataType::UInt32 => impl_add_one(s.u32().unwrap()),
        DataType::UInt64 => impl_add_one(s.u64().unwrap()),
        DataType::Int32 => impl_add_one(s.i32().unwrap()),
        DataType::Int64 => impl_add_one(s.i64().unwrap()),
        DataType::Float32 => impl_add_one(s.f32().unwrap()),
        DataType::Float64 => impl_add_one(s.f64().unwrap()),
        dtype => {
            polars_bail!(InvalidOperation:format!("dtype {dtype} not \
            supported for `add_one`, expected UInt32, UInt64, Int32, Int64, Float32, Float64."))
        }
    }
    Ok(out.into_series())
}

