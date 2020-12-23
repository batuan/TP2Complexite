
/* Graph generator submitted by Mark Brockington and Joe Culberson

For using:

  ./graphgen -gxxxx -cxxxx -px.xxxxxx -dx -sxxxx

ex: ./graphgen -g00150 -c4 -p0.200 -d0 -s0 

will generator graph 150 vertices, with edge density is 0.2

arg is of the form: -gxxxx     (Graph Size)
                    -cxxxx     (Clique Size)
                    -px.xxxxxx (Edge Density Requested)
                    -dx        (Defender Type)
                    -sxxxx     (Seed Number)

Defaults: -g1000 -i16 -p0.500 -d0 -s0


Because the out put is binary format, so we can use the tools bin2acs write by Tamas Badics.

using: 
	./bin2asc src.txt dst.txt

src.txt: file bin binary format
dst.txt: out put file with ascii