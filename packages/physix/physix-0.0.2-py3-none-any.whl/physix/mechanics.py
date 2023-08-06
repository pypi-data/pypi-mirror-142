import numpy as np
from scipy.integrate import solve_ivp


def solve_newton_ivp(force, times, x0, v0, m):
    """ Solve the Newtonian equations of motion for given initial conditions.

    Parameters
    ----------
    force: callable
        Function with signature (t, x, v) to calculate the force(s)
    times: numpy.ndarray
        A 1D numpy array with the times where to calculate the solution
    x0: numpy.ndarray
        Initial position(s); array of shape (nbodies, ndims) or (ndims,) or just
        a scalar.
    v0: numpy.ndarray
        Initial velocities; same shape as x0
    m: float or np.ndarray 1D
        The mass or the masses of the particle(s)

    Returns
    -------
    x, v:  tuple of np.ndarrays
        Time evolution of positions and velocities. Shape is (nbodies, ndims, :)
        or (ndims, :) or (:) where : is the axis for the time steps.

    """

    if not hasattr(m, '__len__'):
        nbodies = 1
    else:
        nbodies = len(m)

    if nbodies == 1:
        if hasattr(x0, '__len__'):
            ndims = len(x0)
            y0 = np.vstack((x0.reshape(-1), v0.reshape(-1))).reshape(-1)
        else:
            ndims = 1
            y0 = np.vstack((x0, v0)).reshape(-1)
    else:
        _, ndims = x0.shape
        assert x0.shape == v0.shape
        assert len(x0) == nbodies

        y0 = np.vstack((x0.reshape(-1), v0.reshape(-1))).reshape(-1)

    if hasattr(m, '__len__'):
        m_ = np.ones((nbodies, ndims))
        for dim in range(ndims):
            m_[:, dim] = m.copy()
        m = m_
    else:
        m = m * np.ones(nbodies*ndims)

    def f(t, y):
        n = len(y) // 2
        x = y[:n]
        v = y[n:]
        ff = force(t, x.reshape(nbodies, ndims), v.reshape(nbodies, ndims))
        ydot = np.vstack((v, ff.reshape(-1))).reshape(-1)
        ydot[n:] /= m.reshape(-1)
        return ydot

    sol = solve_ivp(f, (times[0], times[-1]), y0, t_eval=times, rtol=1.e-6)
    nn = nbodies * ndims
    x, v = sol.y[:nn], sol.y[nn:]

    if nbodies == 1:
        if ndims == 1:
            return x.reshape(-1), v.reshape(-1)
        else:
            return x.reshape(ndims, -1), v.reshape(ndims, -1)
    return x.reshape(nbodies, ndims, -1), v.reshape(nbodies, ndims, -1)