use std::fs;


pub fn template(puzzle_input: &str) -> (i64, i64) {
    let mut a: i64 = 0;
    let mut b: i64 = 0;

    let stream: String = fs::read_to_string(puzzle_input)
        .expect(&format!("Unable to parse file {}!", puzzle_input));

    let mut mat: Vec<Vec<i64>> = Vec::new();

    for line in stream.split('\n') {
        let splitted: Vec<&str> = line.split(' ').collect();
        if splitted.is_empty() { continue; }


        let line = splitted
            .iter()
            .map(|x| x.trim().parse::<i64>()
                .expect(&format!("Failed to parse '{x}'!"))
            )
            .collect();

        mat.push(line);
    }

    for v in mat {

        a += is_safe(&v) as i64;
        b += is_safe(&v) as i64;

        if !is_safe(&v) {
            let mut safety = false;
            for i in 0..(v.len()-1) {
                let new_vec: Vec<i64> = [&v[..i], &v[i+1..]].concat();
                if is_safe(&new_vec) {
                    safety = true;
                    break;
                }
            }
            b += safety as i64;
        } 
        
    }
    return (a, b);
}


fn is_safe(line: &Vec<i64>) -> bool {
    if line[1] == line[0] { return false; }
    let direction = line[1] > line[0];
    
    for i in 2..line.len() {
        let diff = (line[i]-line[i-1]).abs();
        if ((line[i] > line[i-1]) != direction) || (diff > 3) || (diff < 1) {
            return false;
        }  
    }
    return true;
}
