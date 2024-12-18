use std::fs;


pub struct FileInput {
    pub stream: String
}

impl FileInput {
    pub fn new(path: &str) -> Self {
        let stream = fs::read_to_string(path)
            .expect(&format!("Unable to read file from {path}"));

        return Self { stream }
    }

    pub fn read_to_matrix(&self) -> Vec<Vec<char>> {
        let mut output: Vec<Vec<char>> = Vec::new();

        for line in self.stream.split('\n') {
            output.push(line.chars().collect());
        }

        return output;
    }
}

