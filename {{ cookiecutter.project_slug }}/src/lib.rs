mod expressions;
use pyo3::types::{PyModule, PyModuleMethods};
use pyo3::{pymodule, Bound, PyResult};
use pyo3_polars::PolarsAllocator;

#[pymodule]
fn _internal(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}

#[global_allocator]
static ALLOC: PolarsAllocator = PolarsAllocator::new();

