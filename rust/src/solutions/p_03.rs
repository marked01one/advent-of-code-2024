use std::fs;
use chrono::Utc;
use regex::Regex;

pub fn template(input: &str) -> (i64, i64, i64) {
    let start = Utc::now();

    let mut a: i64 = 0;
    let mut b: i64 = 0;

    let stream = fs::read_to_string(input)
        .expect(&format!("Unable to read file from path: {input}!"));
    
    let re = Regex::new(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
        .expect("Unable to convert string to regex!");
    
    let matches: Vec<&str> = re
        .find_iter(&stream)
        .map(|mat| mat.as_str())
        .collect();

    let mut enabled = true;

    for mat in matches {
        match mat {
            "do()" => enabled = true,
            "don't()" => enabled = false,
            _ => {
                let nums: Vec<i64> = mat[4..mat.len()-1]
                    .split(',')
                    .map(|n| n.parse::<i64>()
                        .expect(&format!("Unable to parse string {n}!"))
                    )
                    .collect();
                
                a += nums[0] * nums[1];
                if enabled { b += nums[0] * nums[1] } 
            }
        }
    }

    
    let span = (Utc::now()-start)
        .num_microseconds()
        .expect("Unable to get microsecond time delta!");

    return (a, b, span);
}