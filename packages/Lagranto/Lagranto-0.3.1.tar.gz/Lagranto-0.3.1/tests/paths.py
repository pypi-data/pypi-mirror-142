# define paths to use in different files

from datetime import datetime

from path import Path

testdatadir = Path.dirname(Path(__file__)).joinpath("test_data")

netcdffile = testdatadir / "lsl_lagranto2_0.nc"
asciifile = testdatadir / "lsl_lagranto2_0.txt"

longasciifile = testdatadir / "lsl_long_ASCII.txt"

asciifile_minutes = testdatadir / "lsl_lagranto2_0_minutes.txt"
netcdffile_minutes = testdatadir / "lsl_lagranto2_0_minutes.nc"

gzipfile = testdatadir / "lsl_lagranto2_0.txt.gz"

onlinefile = testdatadir / "lsl_lagranto_online.nc"

backfile = testdatadir / "lsl_lagranto_backward_forward.txt.gz"

wrong_timestep_file = testdatadir / "lsl_wrong_timestep.txt"
wrong_ntra_file = testdatadir / "lsl_wrong_ntra.txt"

var_start_file = testdatadir / "lsl_var_start.txt"

startdate = datetime(2000, 10, 14, 6)
