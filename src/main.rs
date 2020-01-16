#![feature(test)]
extern crate test;

mod problems;

fn main() {
    println!("Hi, you are running 'cargo run' but should use 'cargo bench' to see the performance of the solutions.")
}

#[cfg(test)]
mod tests {
    use super::*;
    #[allow(unused_imports)]
    use test::Bencher;
}
