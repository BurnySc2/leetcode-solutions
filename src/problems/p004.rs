pub struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // Merge the two vecs
        let mut nums3 = vec![];
        let (mut index1, mut index2) = (0, 0);
        let (limit1, limit2) = (nums1.len(), nums2.len());
        while index1 < limit1 || index2 < limit2 {
            // index1 reached the end of nums1
            if index1 == limit1 {
                nums3.push(nums2[index2]);
                index2 += 1;
            // index2 reached the end of nums2
            } else if index2 == limit2 {
                nums3.push(nums1[index1]);
                index1 += 1;
            } else {
                // index1 and index2 are both within the array
                if nums1[index1] < nums2[index2] {
                    nums3.push(nums1[index1]);
                    index1 += 1;
                } else {
                    nums3.push(nums2[index2]);
                    index2 += 1;
                }
            }
        }
        let length = nums3.len();
        if length % 2 == 1 {
            nums3[length / 2] as f64
        } else {
            ((nums3[length / 2] + nums3[length / 2 - 1]) as f64) / 2.0
        }
    }
}

fn test_solution() {
    //    let nums1: Vec<i32> = vec![1, 3];
    //    let nums2: Vec<i32> = vec![2];
    let nums1 = vec![1, 2];
    let nums2 = vec![3, 4];

    //    s = Solution{};
    let solution = Solution::find_median_sorted_arrays(nums1, nums2);
    println!("{:?}", solution);
}

fn main() {
    //    println!("Hello, world!");
    test_solution();
}
