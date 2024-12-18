use std::collections::HashMap;
use chrono::Utc;
use crate::utils::file::FileInput;


pub fn template(path: &str) -> (i64, i64, i64) {
    let start = Utc::now();

    let mut a: i64 = 0;
    let mut b: i64 = 0;

    let fp = FileInput::new(path);

    let mut arr1: Vec<i32> = vec![];
    let mut arr2: Vec<i32> = vec![];
    let mut hashmap: HashMap<i32, i32> = HashMap::new();
    
    for line in fp.stream.split('\n') {
        let splitted: Vec<&str> = line.split("   ").collect();
        arr1.push(splitted[0].parse::<i32>().expect("Left element of line not found!"));
        arr2.push(splitted[1].parse::<i32>().expect("Right element of line not found!"));
    }

    assert_eq!(arr1.len(), arr2.len(), "Input arrays mismatched! {} != {}", arr1.len(), arr2.len());

    arr1.sort(); arr2.sort();

    for n2 in arr2.iter() { *hashmap.entry(*n2).or_insert(0) += 1 }

    for i in 0..arr1.len() {
        a += (arr1[i]-arr2[i]).abs() as i64;
        b += (arr1[i] * *hashmap.get(&arr1[i]).get_or_insert(&0)) as i64;
    }

    let span = (Utc::now()-start)
        .num_microseconds()
        .expect("Unable to get microsecond time delta!");

    return (a, b, span);
}