help('modules')

import math

help(math)

math.factorial(5)
math.sqrt(5)

print(math.sqrt.__doc__)

import statistics # tum statistics modulunu ımport eder

import statistics as st # modulu st olarak cagır

st.median([23, 45, 23, 12, 6])

from statistics import median # modulden istenilen func cagırma
median([23, 45, 23, 12, 6])

from statistics import median, mean
median([23, 45, 23, 12, 6])
mean([23, 45, 23, 12, 6])