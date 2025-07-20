# verilog_instance_from_module
A python script that reads a verilog module definition and prints the instance ports in neat columns. User is responsible for naming the instance and terminating it. The instance does not duplicate port comments, it just provides the port attributes necessary for connection as comments. All verilog/systemverilog instances should look this way... no need for port names to have suffixes which indicate direction, as width information is also needed (and width is sometimes parameterized).

**Example input** (the real input can be the entire module defintion, just the header is shown here):
````
module tap_counter_debounced #(
  parameter int COUNT_WIDTH     = 8
) (
  input  logic                   clk,
  input  logic                   rst_n,        // active-low sync reset
  input  logic                   button_raw,   // async, bouncing input
  output logic [COUNT_WIDTH-1:0] count,        // total taps counted
  output logic                   done          // one-clk pulse on timeout
);
````
**Example output**:
````
.clk        (),          \\ input  
.rst_n      (),          \\ input  
.button_raw (),          \\ input  
.count      (),          \\ output [COUNT_WIDTH-1:0]
.done       (),          \\ output 
````
