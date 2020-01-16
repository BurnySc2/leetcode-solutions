pub struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let mut n = x;
        let mut a = 0;
        while n > 0 {
            let r = n % 10;
            n = n / 10;
            a = a * 10 + r;
        }
        if a == x {
            return true;
        }
        return false;
    }
}
