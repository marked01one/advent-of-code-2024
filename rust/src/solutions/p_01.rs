use std::collections::HashMap;
use std::fs;


pub fn template(puzzle_input: &str) -> (i32, i32) {
    let mut a = 0;
    let mut b = 0;

    let stream = fs::read_to_string(puzzle_input)
        .expect(&format!("Unable to parse file {}!", puzzle_input));

    let mut arr1: Vec<i32> = vec![];
    let mut arr2: Vec<i32> = vec![];
    let mut hashmap: HashMap<i32, i32> = HashMap::new();
    
    for line in stream.split('\n') {
        let splitted: Vec<&str> = line.split("   ").collect();
        arr1.push(splitted[0].parse::<i32>().expect("Left element of line not found!"));
        arr2.push(splitted[1].parse::<i32>().expect("Right element of line not found!"));
    }

    assert_eq!(arr1.len(), arr2.len(), "Input arrays mismatched! {} != {}", arr1.len(), arr2.len());

    arr1.sort(); arr2.sort();

    for n2 in arr2.iter() { *hashmap.entry(*n2).or_insert(0) += 1 }

    for i in 0..arr1.len() {
        a += (arr1[i]-arr2[i]).abs();
        b += arr1[i] * *hashmap.get(&arr1[i]).get_or_insert(&0);
    }

    return (a, b);
}