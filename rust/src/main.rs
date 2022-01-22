use std::io;

fn main() {
    let mut input_text = String::new();
    io::stdin()
        .read_line(&mut twi input_text)
        .expect("failed to read from stdin");

    let trimmed = input_text.trim();
    match trimmed.parse::<u32>() {
        Ok(i) => println!("your integer input: {}", i),
        Err(..) => println!("this was ont an integer: {}", trimmed)
    };


}
