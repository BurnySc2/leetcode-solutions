pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            for j in (i + 1)..nums.len() {
                if (nums[i] + nums[j] == target) {
                    result.push(i as i32);
                    result.push(j as i32);
                    return result;
                }
            }
        }
        return result;
    }
}

fn run_001() {
    // Problem 001
    let solution = Solution::two_sum(vec![2, 7, 11, 15], 9);
    assert_eq!(solution, vec![0, 1]);
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
}
