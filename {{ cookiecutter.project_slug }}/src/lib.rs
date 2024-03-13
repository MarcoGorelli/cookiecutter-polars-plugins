mod expressions;
mod utils;

#[cfg(target_os = "linux")]
use jemallocator::Jemalloc;

#[global_allocator]
#[cfg(target_os = "linux")]
static ALLOC: Jemalloc = Jemalloc;

use pyo3::types::PyModule;
use pyo3::{pymodule, PyResult, Python};

#[pymodule]
fn mymodule(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}