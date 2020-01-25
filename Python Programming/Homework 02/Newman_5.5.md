###Newman Problem 5.5

The Euler-Maclaurin formula for Simpson's Rule shows that the error is of order $O(h^4)$:

$$
\epsilon = \frac{1}{90}h^4[f'''(a) - f'''(b)]
$$

Suppose the actual value of some integral is $I$. Since order of error on Simpsons rule is $h^4$ , our estimate $I_1 $ with $N_1$ steps yields:

$$
I - I_1 = ch_1^4
$$

If we let $N_2 = 2N_1$, then $h_2 = \frac{1}{2}h_1$ and the new error is one-sixteenth of the previous error. We get another equation:

$$
I - I_2 = ch_2^4
$$

we combine them both with $h_1 = 2h_2$ to yield:

$$
I_2 - I_1 = ch_1^4 - ch_2^4 = 15ch_2^4
$$

rearranging this expression, we can find the error on the second integral with the following:

$$
\epsilon_2 = \frac{1}{15}(I_2 = I_1)
$$
