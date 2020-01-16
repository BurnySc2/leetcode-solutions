#![feature(test)]
extern crate test;

mod problems;

fn run_001() {
    // Problem 001
    let solution = problems::p001_twosum::Solution::two_sum(vec![2, 7, 11, 15], 9);
    assert_eq!(solution, vec![0, 1]);
}

fn run_004_01() {
    // Problem 004
    let solution = problems::p004::Solution::find_median_sorted_arrays(vec![1, 3], vec![2]);
    assert_eq!(solution, 2.0);
}
fn run_004_02() {
    let solution = problems::p004::Solution::find_median_sorted_arrays(vec![1, 2], vec![3, 4]);
    assert_eq!(solution, 2.5);
}
fn run_007_01() {
    let solution = problems::p007::Solution::reverse(123);
    assert_eq!(solution, 321);
}
fn run_007_02() {
    let solution = problems::p007::Solution::reverse(-123);
    assert_eq!(solution, -321);
}
fn run_007_03() {
    let solution = problems::p007::Solution::reverse(120);
    assert_eq!(solution, 21);
}

fn main() {
    println!("Hi, you are running 'cargo run' but should use 'cargo bench' to see the performance of the solutions.")
}

#[cfg(test)]
mod tests {
    use super::*;
    #[allow(unused_imports)]
    use test::Bencher;

    // This will only be executed when using "cargo test" and not "cargo bench"
    #[bench]
    fn bench_run_001(b: &mut Bencher) {
        b.iter(|| run_001());
    }
    #[bench]
    fn bench_run_004_01(b: &mut Bencher) {
        b.iter(|| run_004_01());
    }
    #[bench]
    fn bench_run_004_02(b: &mut Bencher) {
        b.iter(|| run_004_02());
    }
    #[bench]
    fn bench_run_007_01(b: &mut Bencher) {
        b.iter(|| run_007_01());
    }
    #[bench]
    fn bench_run_007_02(b: &mut Bencher) {
        b.iter(|| run_007_02());
    }
    #[bench]
    fn bench_run_007_03(b: &mut Bencher) {
        b.iter(|| run_007_03());
    }
}
