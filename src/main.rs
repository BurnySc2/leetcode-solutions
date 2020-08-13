#![feature(test)]
extern crate test;

mod problems;

// To generate assembly code:
// cargo rustc -- --emit asm
// Optimized:
// cargo rustc --release -- --emit asm

// Test:
// cargo test
// Bench:
// cargo bench

fn main() {
    println!("Hi, you are running 'cargo run' but should use 'cargo bench' to see the performance of the solutions.");
}

#[cfg(test)]
mod tests {
    use super::*;
    #[allow(unused_imports)]
    use test::Bencher;
}
