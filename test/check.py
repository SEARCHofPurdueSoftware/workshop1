import sys
import json
from colors import bcolors

# This should only be invoked via `make *`!
if __name__ == "__main__":
	ARGS = sys.argv

	TESTNAME = ARGS[1]

	f = open("test/" + TESTNAME + ".json")
	CONFIG = json.load(f)
	f.close()

	f = open("results/" + TESTNAME + ".results")
	RESULTS_RAW = f.read().split("\n")
	f.close()

	results = []

	for result in RESULTS_RAW:
		if result == '':
			continue
		beg = result.index("<")
		end = result.index(">")
		out = result[beg + 1:end].replace(" ", "")
		while " " in out:
			out = out.replace(" ", "")
		results.append(out)


	expected = CONFIG["expected"]

	print(bcolors.OKCYAN, end = '')
	print("*" * 27)
	print("** BEGINNING CODE TESTS **")
	print("*" * 27)
	print(bcolors.ENDC, end = '')

	passed = True

	for ind, exp in expected.items():
		act = results[int(ind)]
		if act == exp:
			print(bcolors.OKBLUE, "Test %d passed!" % (int(ind) + 1), bcolors.ENDC)
		else:
			print(bcolors.FAIL, "Test %s failed! Got incorrect value <%s>." % (ind, act), bcolors.ENDC)
			passed = False

	if passed:
		print(''' 
O----------------------------------------------------------O
| .              +   .                .   . .     .  .     |
|                   .                    .       .     *   |
|  .       *                        . . . .  .   .  + .    |
|                                      .   .  +  . . .     |
|.                               .  .   .    .    . .      |
|                              .     .     . +.    +  .    |
|      \033[92m***  * *  ***  ***  ***  ***  ***\033[0m     .   . .       |
|      \033[92m*    * *  *    *    *    *    * \033[0m* . . .  .  +   .   |
|      \033[92m*** \033[0m+\033[92m* *  *    *    ***  ***  ***\033[0m      +            |
|        \033[92m*  * *  *    *    *      *    *\033[0m . +  .+. .        |
|  .   \033[92m***  ***  ***  ***  ***  ***  ***\033[0m.  . .     .      .|
|           .      .    .     . .   . . .        ! /       |
|      *             .    . .  +    .  .       - O -       |
|          .     .    .  +   . .  *  .       . / |         |
|               . + .  .  .  .. +  .                       |
|.      .  .  .  *   .  *  . +..  .            *           |
| .      .   . .   .   .   . .  +   .    .            +    |
O----------------------------------------------------------O
			''')

