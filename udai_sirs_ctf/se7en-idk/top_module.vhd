----------------------------------------------------------------------------------
--Se7en : Find the message "displayed" by the killer!!
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity et is
  Port ( 
        a : in std_logic;
        b : in std_logic;
        c : out std_logic
  );
end et;

architecture Behavioral of et is

begin

c <= a and b;

end Behavioral;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity porta is
  Port ( 
        d : in std_logic;
        e : in std_logic;
        f : out std_logic
  );
end porta;

architecture Behavioral of porta is
begin
f <= d or e;
end Behavioral;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity non is
  Port ( 
        g : in std_logic;
        h : out std_logic
  );
end non;

architecture Behavioral of non is

begin
h <= not g;
end Behavioral;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity neque is
  Port ( 
        i : in std_logic;
        j : in std_logic;
        k : out std_logic
  );
end neque;

architecture Behavioral of neque is

begin
k <= not(i or j);
end Behavioral;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity aut is
  Port ( 
        l : in std_logic;
        m : in std_logic;
        n : out std_logic
  );
end aut;

architecture Behavioral of aut is

begin
n <= l xor m;
end Behavioral;


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity nonet is
  Port ( 
        o : in std_logic;
        p : in std_logic;
        q : out std_logic
  );
end nonet;

architecture Behavioral of nonet is

begin
q <=  not (o and p);
end Behavioral;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity non_aut is
port (
    r : in std_logic;
    s : in std_logic;
    t : out std_logic
);
end non_aut;
architecture Behavioral of non_aut is

begin
t <= not( r xor s);
end Behavioral;


------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity top is
    port(
        in1 : in std_logic;
        in2 : in std_logic;
        in3 : in std_logic;
        in4 : in std_logic;
        in5 : in std_logic;
        in6 : in std_logic;
        in7 : in std_logic;
        in8 : in std_logic;
        
        out1 : out std_logic;
        out2 : out std_logic;
        out3 : out std_logic;
        out4 : out std_logic;
        out5 : out std_logic;
        out6 : out std_logic;
        out7 : out std_logic;
        out8 : out std_logic
        
    );
   end top;
   
architecture behave of  top is 
signal temp1 : std_logic;
signal temp2 : std_logic;
signal temp3 : std_logic;
signal temp4 : std_logic;
signal temp5 : std_logic;
signal temp6 : std_logic;
signal temp7 : std_logic;
signal temp8 : std_logic;
signal temp9 : std_logic;
signal temp10 : std_logic;
signal temp11 : std_logic;
signal temp12 : std_logic;
signal temp13 : std_logic;
signal temp14 : std_logic;
signal temp15 : std_logic;
signal temp16 : std_logic;
signal temp17 : std_logic;
signal temp18 : std_logic;
signal temp19 : std_logic;
signal temp20 : std_logic;
signal temp21 : std_logic;
signal temp22 : std_logic;
signal temp23 : std_logic;
signal temp24 : std_logic;
signal temp25 : std_logic;
signal temp26 : std_logic;
signal temp27 : std_logic;
signal temp28 : std_logic;
signal temp29 : std_logic;
signal temp30 : std_logic;



begin
   
   one : entity work.et(Behavioral)
   port map(
   a => in1,
   b => in2,
   c => temp1
   );
   
   two : entity work.aut(Behavioral)
   port map(
    l => temp1,
    m => in2,
    n => temp2
   ); 
   
   three: entity work.porta(Behavioral)
   port map(
   d => temp2,
   e => in1,
   f => out1
     );
    
   four : entity work.non(Behavioral)
   port map(
   g => in2,
   h => temp3
   );
   
   five : entity work.porta(Behavioral)
   port map(
   d => temp3,
   e => temp3,
   f => temp4
   );
     
   six : entity work.nonet(Behavioral)
   port map(
   o => temp4,
   p => temp4,
   q => temp5
   );
    
   seven : entity work.aut(Behavioral)
   port map(
   l => temp5,
   m => in2,
   n => out2
   );
   
   -- Two bits
   
   eight : entity work.non(Behavioral)
   port map(
   g => in3,
   h => temp6
   );
   
   nine : entity work.et(Behavioral)
   port map(
   a => temp6,
   b => temp6,
   c => temp7
   );
   
   ten : entity work.neque(Behavioral)
   port map(
   i => temp7,
   j => temp7,
   k => temp8
   );
   
   eleven : entity work.non_aut(Behavioral)
   port map(
   r => temp8,
   s => temp6,
   t => out3
   );
   
   twelve : entity work.nonet(Behavioral)
   port map(
   o => in4,
   p => in5,
   q => temp9
   );
   
   thirteen : entity work.nonet(Behavioral)
   port map(
   o => temp9,
   p => in5,
   q => temp10
   );
   
   fourteen : entity work.nonet(Behavioral)
   port map(
   o => temp10,
   p => in1,
   q => temp11
   );
   
   fifteen : entity work.nonet(Behavioral)
   port map(
   o => temp11,
   p => in5,
   q => out4
   );
   
   sixteen : entity work.et(Behavioral)
   port map(
   a => in5,
   b => in5,
   c => temp12
   );
   
   seventeen : entity work.nonet(Behavioral)
   port map(
   o => temp12,
   p => temp12,
   q => temp13
   );
   
   eighteen : entity work.non(Behavioral)
   port map(
   g => temp13,
   h => temp14
   );
   
   nineteen : entity work.aut(Behavioral)
   port map(
   l => temp13,
   m => temp14,
   n => temp15
   );
   
   twenty : entity work.porta(Behavioral)
   port map(
   d => temp14,
   e => temp15,
   f => out5
   );
   
   --5 bits over
   
   twenty_one : entity work.et(Behavioral)
   port map(
   a => in6,
   b => in7,
   c => temp17
   );
   
   twenty_two : entity work.non(Behavioral)
   port map(
   g => temp17,
   h => temp18
   );
   
   twenty_three : entity work.et(Behavioral)
   port map(
   a => temp18,
   b => temp18,
   c => temp19
   );
   
   twenty_four : entity work.et(Behavioral)
   port map(
   a => temp19,
   b => temp19,
   c => out6
   );
   
   twenty_five : entity work.non_aut(Behavioral)
   port map(
   r => in5,
   s => in7,
   t => temp20
   );
   
   twenty_six : entity work.porta(Behavioral)
   port map(
   d => temp20,
   e => in5,
   f => temp21
   );
   
   twenty_seven : entity work.non(Behavioral)
   port map(
   g => in7,
   h => temp22
   );
   
   twenty_eight : entity work.nonet(Behavioral)
   port map(
   o => temp22,
   p => temp21,
   q => out7
   );
   
   twenty_nine : entity work.aut(Behavioral)
   port map(
   l => in7,
   m => in8,
   n => temp23
   );
   
   thirty : entity work.et(Behavioral)
   port map(
   a => in7,
   b => temp23,
   c => temp24
   );
   
   thirty_one: entity work.non(Behavioral)
   port map(
   g => in8,
   h => temp25
   );
   thirty_two : entity work.neque(Behavioral)
   port map(
   i => temp25,
   j => temp24,
   k => out8
   );
end behave;
   
   
