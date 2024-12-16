mod solutions;


fn main() {
    let (a_01, b_01, time_01) = solutions::p_01::template("../../01.txt");
    let (a_02, b_02, time_02) = solutions::p_02::template("../../02.txt");
    let (a_03, b_03, time_03) = solutions::p_03::template("../../03.txt");
    
    println!("RESULTS");
    println!("* 01: ({a_01}, {b_01})\t[{} ms]", (time_01 as f64) / 1000.0);
    println!("* 02: ({a_02}, {b_02})\t\t[{} ms]", (time_02 as f64) / 1000.0);
    println!("* 03: ({a_03}, {b_03})\t[{} ms]", (time_03 as f64) / 1000.0);
}
