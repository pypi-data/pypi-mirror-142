import numpy as np
from astropy.cosmology import Planck18 as cosmo  # noqa

import scipy.special as ss
from scipy.integrate import quad
from inspect import isfunction
from redback.utils import logger, citation_wrapper

from redback.constants import *
from redback.transient_models.fireball_models import one_component_fireball_model

luminosity_models = ['evolving_magnetar', 'evolving_magnetar_only', 'gw_magnetar', 'radiative_losses',
                     'radiative_losses_smoothness', 'radiative_only', 'collapsing_radiative_losses']


def _mu_function(time, mu0, muinf, tm):
    mu = muinf + (mu0 - muinf) * np.exp(-time / tm)
    return mu


def _integrand(time, mu0, muinf, tm):
    mu = muinf + (mu0 - muinf) * np.exp(-time / tm)
    return mu ** 2

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2019ApJ...886....5S/abstract')
def _evolving_magnetar_only(time, mu0, muinf, p0, sinalpha0, tm, II, **kwargs):
    """
    Millisecond magnetar model with evolution of inclination angle

    :param time: time in seconds
    :param mu0: Initial magnetic moment [10^33 G cm^3]
    :param muinf: Magnetic moment when field relaxes [10^33 G cm^3]
    :param p0: initial spin period
    :param sinalpha0: initial sin(alpha0) where alpha is the angle between B and P axes.
    :param tm: magnetic field decay timescale in days
    :param II: Moment of inertia in cgs
    :param kwargs: key word argument for handling plotting
    :return: luminosity (depending on scaling) as a function of time.
    """
    mu0 = mu0 * 1e33  # G cm^3
    muinf = muinf * 1e33  # G cm^3
    tm = tm * 86400  # days
    eta = 0.1
    tau = np.zeros(len(time))
    for ii in range(len(time)):
        tau[ii], _ = quad(_integrand, 0, time[ii], args=(mu0, muinf, tm)) # noqa
    mu = _mu_function(time, mu0, muinf, tm)
    omega0 = (2 * np.pi) / p0
    tau = (omega0 ** 2) / (II * speed_of_light ** 3) * tau
    y0 = sinalpha0
    common_frac = (np.log(1 + 2 * tau) - 4 * tau) / (1 + 2 * tau)
    ftau = 2 * (1 - y0 ** 2) ** 2 * tau
    + y0 ** 2 * np.log(1 + 2 * tau)
    + y0 ** 4 * common_frac
    - y0 ** 8 * (np.log(1 + 2 * tau) + common_frac)
    ytau = y0 / ((1 + ftau) ** 0.5)
    omegatau = omega0 * (1 - y0 ** 2) * ((1 + ftau) ** 0.5) / (1 - y0 ** 2 + ftau)
    luminosity = eta * (mu ** 2 * omegatau ** 4) / (speed_of_light ** 3) * (1 + ytau ** 2)
    return luminosity / 1e50

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2019ApJ...886....5S/abstract')
def evolving_magnetar(time, a_1, alpha_1, mu0, muinf, p0, sinalpha0, tm, II, **kwargs):
    """
    Millisecond magnetar model with evolution of inclination angle

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param mu0: Initial magnetic moment [10^33 G cm^3]
    :param muinf: Magnetic moment when field relaxes [10^33 G cm^3]
    :param p0: initial spin period
    :param sinalpha0: initial sin(alpha0) where alpha is the angle between B and P axes.
    :param tm: magnetic field decay timescale in days
    :param II: Moment of inertia in cgs
    :param kwargs: key word argument for handling plotting
    :return: luminosity (depending on scaling) as a function of time.
    """
    pl = one_component_fireball_model(time=time, a_1=a_1, alpha_1=alpha_1)
    magnetar = _evolving_magnetar_only(time=time, mu0=mu0, muinf=muinf,
                                       p0=p0, sinalpha0=sinalpha0, tm=tm, II=II)
    return pl + magnetar

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2017ApJ...843L...1L/abstract')
def _magnetar_only(time, l0, tau, nn, **kwargs):
    """
    :param time: time in seconds
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity or flux (depending on scaling of l0) as a function of time.
    """
    lum = l0 * (1. + time / tau) ** ((1. + nn) / (1. - nn))
    return lum

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2018PhRvD..98d3011S/abstract')
def gw_magnetar(time, a_1, alpha_1, fgw0, tau, nn, log_ii, **kwargs):
    """
    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param fgw0: initial gravitational-wave frequency
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param log_ii: log10 moment of inertia
    :param eta: fixed to 0.1, its a fudge factor for the efficiency
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity
    """
    eta = 0.1
    omega_0 = fgw0 * np.pi  # spin frequency
    ii = 10 ** log_ii
    l0 = ((omega_0 ** 2) * eta * ii) / (2 * tau)
    l0_50 = l0 / 1e50

    magnetar = _magnetar_only(time=time, l0=l0_50, tau=tau, nn=nn)
    pl = one_component_fireball_model(time=time, a_1=a_1, alpha_1=alpha_1)

    return pl + magnetar

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2017ApJ...843L...1L/abstract')
def full_magnetar(time, a_1, alpha_1, l0, tau, nn, **kwargs):
    """
    Generalised millisecond magnetar with curvature effect power law

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity or flux (depending on scaling of l0) as a function of time.
    """
    pl = one_component_fireball_model(time=time, a_1=a_1, alpha_1=alpha_1)
    mag = _magnetar_only(time=time, l0=l0, tau=tau, nn=nn)
    return pl + mag

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020PhRvD.101f3021S/abstract')
def collapsing_magnetar(time, a_1, alpha_1, l0, tau, nn, tcol, **kwargs):
    """
    Generalised millisecond magnetar with curvature effect power law and a collapse time

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param tcol: collapse time in seconds
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity or flux (depending on scaling of l0) as a function of time.
    """
    pl = one_component_fireball_model(time, a_1, alpha_1)
    mag = np.heaviside(tcol - time, 1e-50) * _magnetar_only(time, l0, tau, nn)

    return pl + mag

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2019ApJ...872..114S/abstract')
def general_magnetar(time, a_1, alpha_1,
                     delta_time_one, alpha_2, delta_time_two, **kwargs):
    """
    Reparameterized millisecond magnetar model (piecewise)

    :param time: time array for power law
    :param a_1: power law decay amplitude
    :param alpha_1: power law decay exponent
    :param delta_time_one: time between start and end of prompt emission
    :param alpha_2: Reparameterized braking index n
    :param delta_time_two: time between end of prompt emission and end of magnetar model plateau phase, (tau)
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity or flux (depending on scaling of l0) as a function of time.
    """

    time_one = delta_time_one
    tau = delta_time_one + delta_time_two
    nn = (alpha_2 - 1.) / (alpha_2 + 1.)
    gamma = (1. + nn) / (1. - nn)
    num = (a_1 * time_one ** alpha_1)
    denom = ((1. + (time_one / tau)) ** gamma)
    a_2 = num / denom

    w = np.where(time < time_one)
    x = np.where(time > time_one)

    f1 = a_1 * time[w] ** alpha_1
    f2 = a_2 * (1. + (time[x] / tau)) ** gamma
    return np.concatenate((f1, f2))

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def _integral_general(time, t0, kappa, tau, nn, **kwargs):
    """
    General integral for radiative losses model

    :param time: time in seconds
    :param t0: time for radiative losses to start in seconds
    :param kappa: radiative efficiency
    :param tau: spin down damping timescale in seconds
    :param nn: braking index
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity
    """
    first_term, second_term = _get_integral_terms(time=time, t0=t0, kappa=kappa, tau=tau, nn=nn)
    return first_term - second_term

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def _integral_general_collapsing(time, t0, kappa, tau, nn, tcol, **kwargs):
    """
    General integral for radiative losses model

    :param time: time in seconds
    :param t0: time for radiative losses to start in seconds
    :param kappa: radiative efficiency
    :param tau: spin down damping timescale in seconds
    :param nn: braking index
    :param tcol: collapse time in seconds
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity
    """
    first_term, second_term = _get_integral_terms(time=time, t0=t0, kappa=kappa, tau=tau, nn=nn)
    return np.heaviside(tcol - time, 1e-50) * (first_term - second_term)

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def _get_integral_terms(time, t0, kappa, tau, nn):
    """
    Get integral terms for radiative losses model

    :param time: time in seconds
    :param t0: time for radiative losses to start in seconds
    :param kappa: radiative efficiency
    :param tau: spin down damping timescale in seconds
    :param nn: braking index
    :return: first and second terms
    """
    alpha = (1 + nn) / (-1 + nn)
    pft = ss.hyp2f1(1 + kappa, alpha, 2 + kappa, -time / tau)
    pst = ss.hyp2f1(1 + kappa, alpha, 2 + kappa, -t0 / tau)
    first_term = (time ** (1 + kappa) * pft) / (1 + kappa)
    second_term = (t0 ** (1 + kappa) * pst) / (1 + kappa)
    return first_term, second_term

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def _integral_mdr(time, t0, kappa, a, **kwargs):
    """
    Calculate integral for vacuum dipole radiation

    :param time: time in seconds
    :param t0: time for radiative losses to start in seconds
    :param kappa: radiative efficiency
    :param a: 1/tau (spin down damping timescale)
    :return: integral
    """
    z_f = (1 + a * time) ** (-1)
    z_int = (1 + a * t0) ** (-1)
    divisor_i = a ** (1 + kappa) * (kappa - 1) * (1 + a * t0) ** (1 - kappa)
    divisor_f = a ** (1 + kappa) * (kappa - 1) * (1 + a * time) ** (1 - kappa)
    first = ss.hyp2f1(1 - kappa, -kappa, 2 - kappa, z_f) / divisor_f
    second = ss.hyp2f1(1 - kappa, -kappa, 2 - kappa, z_int) / divisor_i
    return first - second

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def piecewise_radiative_losses(time, a_1, alpha_1, l0, tau, nn, kappa, t0, **kwargs):
    """
    Assumes smoothness and continuity between the prompt and magnetar term by fixing e0 variable

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param kappa: radiative efficiency
    :param t0: time for radiative losses to start in seconds
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity
    """
    pl_time = np.where(time <= t0)
    magnetar_time = np.where(time > t0)
    e0 = (a_1 * t0 ** alpha_1 * t0) / kappa
    pl = one_component_fireball_model(time[pl_time], a_1, alpha_1)

    loss_term = e0 * (t0 / time[magnetar_time]) ** kappa
    integ = _integral_general(time[magnetar_time], t0, kappa, tau, nn)
    energy_loss_total = ((l0 / (time[magnetar_time] ** kappa)) * integ) + loss_term

    lum = (kappa * energy_loss_total / time[magnetar_time])

    return np.concatenate((pl, lum))

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def radiative_losses(time, a_1, alpha_1, l0, tau, nn, kappa, t0, log_e0, **kwargs):
    """
    radiative losses model with a step function, indicating the magnetar term turns on at T0

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param kappa: radiative efficiency
    :param t0: time for radiative losses to start in seconds
    :param log_e0: log10 E0 to connect curvature effect energy with transition point energy, captures flares
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity
    """
    e0 = 10 ** log_e0
    pl = one_component_fireball_model(time, a_1, alpha_1)
    loss_term = e0 * (t0 / time) ** kappa
    integ = _integral_general(time, t0, kappa, tau, nn)
    energy_loss_total = ((l0 / (time ** kappa)) * integ) + loss_term
    lum = (kappa * energy_loss_total / time)
    total = pl + np.heaviside(time - t0, 1) * lum

    return total

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def radiative_only(time, l0, tau, nn, kappa, t0, log_e0, **kwargs):
    """
    radiative losses model only

    :param time: time in seconds
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param kappa: radiative efficiency
    :param t0: time for radiative losses to start in seconds
    :param log_e0: log10 E0 to connect curvature effect energy smoothly with transition point energy
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity

    :return:
    """
    e0 = 10 ** log_e0
    loss_term = e0 * (t0 / time) ** kappa
    integ = _integral_general(time, t0, kappa, tau, nn)
    energy_loss_total = ((l0 / (time ** kappa)) * integ) + loss_term
    lum = (kappa * energy_loss_total / time)
    total = np.heaviside(time - t0, 1) * lum

    return total

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def radiative_losses_smoothness(time, a_1, alpha_1, l0, tau, nn, kappa, t0, log_e0, **kwargs):
    """
    radiative losses model with a step function, indicating the magnetar term turns on at T0

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param kappa: radiative efficiency
    :param t0: time for radiative losses to start in seconds
    :param log_e0: log10 E0 to connect curvature effect energy smoothly with transition point energy
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity

    """
    pl = one_component_fireball_model(time, a_1, alpha_1)
    e0 = 10 ** log_e0
    e0_def = (a_1 * t0 ** alpha_1 * t0) / kappa
    e0_use = np.min([e0, e0_def])
    loss_term = e0_use * (t0 / time) ** kappa
    integ = _integral_general(time, t0, kappa, tau, nn)

    energy_loss_total = ((l0 / (time ** kappa)) * integ) + loss_term
    lum = (kappa * energy_loss_total / time)
    total = pl + np.heaviside(time - t0, 1) * lum

    return total

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2011A%26A...526A.121D/abstract')
def radiative_losses_mdr(time, a_1, alpha_1, l0, tau, kappa, log_e0, t0, **kwargs):
    """
    radiative losses model for vacuum dipole radiation

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param kappa: radiative efficiency
    :param t0: time for radiative losses to start in seconds
    :param log_e0: log10 E0 to connect curvature effect energy smoothly with transition point energy
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity
    """
    a = 1. / tau
    e0 = 10 ** log_e0
    pl = one_component_fireball_model(time, a_1, alpha_1)
    loss_term = e0 * (t0 / time) ** kappa
    integ = _integral_mdr(time, t0, kappa, a)
    energy_loss_total = ((l0 / (time ** kappa)) * integ) + loss_term

    lightcurve = (kappa * energy_loss_total / time)

    return np.heaviside(time - t0, 1) * lightcurve + pl

@citation_wrapper('https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5986S/abstract')
def collapsing_radiative_losses(time, a_1, alpha_1, l0, tau, nn, tcol, kappa, t0, log_e0, **kwargs):
    """
    radiative losses model with collapse time

    :param time: time in seconds
    :param A_1: amplitude of curvature effect power law
    :param alpha_1: index of curvature effect power law
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index
    :param tcol: collapse time in seconds
    :param kappa: radiative efficiency
    :param t0: time for radiative losses to start in seconds
    :param log_e0: log10 E0 to connect curvature effect energy smoothly with transition point energy
    :param kwargs: key word arguments for handling plotting/other functionality
    :return: luminosity

    """
    e0 = 10 ** log_e0
    pl = one_component_fireball_model(time, a_1, alpha_1)
    loss_term = e0 * (t0 / time) ** kappa
    integ = _integral_general_collapsing(time, t0, kappa, tau, nn, tcol)
    energy_loss_total = ((l0 / (time ** kappa)) * integ) + loss_term
    lum = (kappa * energy_loss_total / time)
    total = pl + np.heaviside(time - t0, 1) * lum

    return total

@citation_wrapper('redback')
def luminosity_based_magnetar_models(time, photon_index, **kwargs):
    """
    Luminosity models that you want to fit to flux data by placing a prior on the redshift.

    :param time: time in observers frame
    :param photon_index: photon index
    :param kwargs: all parameters for the model of choice.
    :return: luminosity/1e50 erg
    """
    from redback.model_library import modules_dict  # import model library in function to avoid circular dependency
    base_model = kwargs['base_model']
    if isfunction(base_model):
        function = base_model
    elif base_model not in luminosity_models:
        logger.warning('{} is not implemented as a base model'.format(base_model))
        raise ValueError('Please choose a different base model')
    elif isinstance(base_model, str):
        function = modules_dict['magnetar_models'][base_model]
    else:
        raise ValueError("Not a valid base model.")
    redshift = kwargs['redshift']
    kcorr = (1 + redshift)**(photon_index - 2)
    dl = cosmo.luminosity_distance(redshift).cgs.value
    time = time / (1 + redshift)
    lum = function(time, **kwargs) * 1e50
    flux = lum / (4*np.pi*dl**2*kcorr)
    return flux
