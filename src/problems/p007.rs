pub struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let is_negative = x < 0;
        let mut a;
        if is_negative {
            a = -x;
        } else {
            a = x;
        }

        // a is now positive, convert to string
        let b: String = a.to_string();
        let mut result: i64 = 0;
        // Loop over string, i is index and c is char
        for (i, c) in b.chars().enumerate() {
            result += ((c as i64 - 48) * (10 as i64).pow(i as u32));
            // println!("{0}, {1}, {2:?}, {3}, {4}", c, i, c as i32 - 48, (10 as i64).pow(i as u32), result);
        }

        // println!("{0}, {1}", result, limit);
        let limit = (2 as i64).pow(31 as u32);
        if result > limit - 1 || result < -limit {
            return 0;
        }

        if is_negative {
            return -result as i32;
        }
        return result as i32;
    }
}
