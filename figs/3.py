import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math

# --- RG parameters --------------------------------------------------------
d = 3
Sd = 2 * np.pi ** (d / 2) / math.gamma(d / 2)
Omega_d = Sd / (2 * np.pi) ** d
Lambda = 10
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'


# --- Auxiliary functions for the RG --------------------------------------
def compute_M(zeta, nu, lam):
    return (1 / (2 * d * (d + 2))) * (
            (d - 2) * (2 * d + 1) * zeta ** 2
            + d * zeta * ((4 - d) * nu + 4 * (d + 2) * lam)
            - (d + 2) * (2 * d * lam * nu - d * nu ** 2 + 4 * lam ** 2)
    )


def compute_T_nu(zeta, nu, lam):
    return (nu / (d * (d + 2))) * (
            (d - 2) * (2 * d + 1) * zeta ** 2
            + d * zeta * ((4 - d) * nu + 4 * (d + 2) * lam)
            - (d + 2) * (2 * d * lam * nu - d * nu ** 2 + 4 * lam ** 2)
    )


def compute_T_lambda(zeta, nu, lam):
    return (nu / (4 * d * (d + 2))) * (
            -2 * (d - 2) * (7 * d + 4) * zeta ** 2
            - 4 * (d + 2) * lam * (2 * (d - 2) * lam - 3 * d * nu)
            - 4 * zeta * (2 * (d * (4 * d + 5) - 10) * lam - (d - 2) * d * nu)
    )


def compute_T_zeta(zeta, nu, lam):
    return (2 * nu * zeta / (4 * d * (d + 2))) * (
            4 * (d - 3) * zeta - 8 * (1 + d) * lam - d * (6 + d) * nu
    )


def compute_B1(u, zeta, nu, lam):
    return (3 * u / (d * (d + 2))) * (
            2 * (4 - d) * zeta - (2 + d) * (4 * lam + d * nu)
    )


def compute_B2_nu(u, zeta, nu, lam):
    return (3 * u / d) * (
            2 * (d - 1) * zeta - (d - 2) * nu
    )


def compute_B2_lambda(u, zeta, nu, lam):
    return (-6 * u / d) * (
            2 * (d - 1) * zeta - (d - 2) * nu
    )


# --- RG right-hand side --------------------------------------------------
def rg_rhs(b, y):
    u, nu, lam, zeta = y
    M = compute_M(zeta, nu, lam)
    T_nu = compute_T_nu(zeta, nu, lam)
    T_l = compute_T_lambda(zeta, nu, lam)
    T_z = compute_T_zeta(zeta, nu, lam)
    B1 = compute_B1(u, zeta, nu, lam)
    B2_nu = compute_B2_nu(u, zeta, nu, lam)
    B2_l = compute_B2_lambda(u, zeta, nu, lam)

    du_db = u * (4 - d) \
            - 9 * u ** 2 * Omega_d * Lambda ** (d - 4) \
            + 2 * u * M * Omega_d * Lambda ** (d - 2)
    dnu_db = nu * ((2 - d) / 2 + 1.5 * M * Omega_d * Lambda ** (d - 2)) \
             + (T_nu * Lambda ** (d - 2)
                + B2_nu * Lambda ** (d - 4)
                + B1 * Lambda ** (d - 4)) * Omega_d
    dlam_db = lam * ((2 - d) / 2 + 1.5 * M * Omega_d * Lambda ** (d - 2)) \
              + 0.5 * (T_l * Lambda ** (d - 2) + B2_l * Lambda ** (d - 4)) * Omega_d
    dzeta_db = zeta * ((2 - d) / 2 + 1.5 * M * Omega_d * Lambda ** (d - 2)) \
               - T_z * Omega_d * Lambda ** (d - 2)

    return [du_db, dnu_db, dlam_db, dzeta_db]


# --- Initial conditions --------------------------------------------------
# Red trajectories (left side, flowing to Wilson-Fisher)
red_initial_conditions = []
for u_start in [3, 6, 9, 12, 15, 18, 21]:
    red_initial_conditions.append([u_start, 0.8 * 3.25, 3.25, 0.52])

# Add the bottom trajectory from (0.52, 0) to (0, 0) - this is also red
red_initial_conditions.append([0, 0.8 * 3.25, 3.25, 0.47])  # This will flow along the bottom

# Blue trajectories (right side)
blue_initial_conditions = []
# Trajectories starting from different u values
for u_start in [4, 8, 12, 18, 25]:
    blue_initial_conditions.append([u_start, 0.8 * 3.25, 3.25, 0.75])

# Add trajectories from the bottom
blue_initial_conditions.append([0, 0.8 * 3.25, 3.25, 0.73])
blue_initial_conditions.append([0, 0.8 * 3.25, 3.25, 0.85])
blue_initial_conditions.append([0, 0.8 * 3.25, 3.25, 1.0])

# --- Integration setup ---------------------------------------------------
b_span = (0.0, 8)
b_eval = np.linspace(b_span[0], b_span[1], 5000)

# --- Solve and plot RG flows in (zeta, u) plane --------------------------
fig, ax = plt.subplots(figsize=(7.5, 6.5))

# Plot red trajectories
for i, y0 in enumerate(red_initial_conditions):
    sol = solve_ivp(rg_rhs, b_span, y0,
                    t_eval=b_eval,
                    method='DOP853',
                    atol=1e-10, rtol=1e-10)
    u_vals = sol.y[0]
    zeta_vals = sol.y[3]

    # Plot trajectory
    plt.plot(zeta_vals, u_vals, lw=1.2, color='red')

    # Add arrow at appropriate position
    if i == len(red_initial_conditions) - 1:  # Last trajectory (bottom one)
        # For the bottom trajectory, place arrow closer to the middle
        arrow_pos = len(zeta_vals) // 2
    else:
        arrow_pos = len(zeta_vals) // 4

    if arrow_pos < len(zeta_vals) - 1:
        ax.annotate(
            '',
            xy=(zeta_vals[arrow_pos + 1], u_vals[arrow_pos + 1]),
            xytext=(zeta_vals[arrow_pos], u_vals[arrow_pos]),
            arrowprops=dict(
                arrowstyle='->',
                lw=1,
                mutation_scale=10,
                shrinkA=0, shrinkB=0,
                color='red'
            ),
        )

# Plot blue trajectories
for i, y0 in enumerate(blue_initial_conditions):
    sol = solve_ivp(rg_rhs, b_span, y0,
                    t_eval=b_eval,
                    method='DOP853',
                    atol=1e-10, rtol=1e-10)
    u_vals = sol.y[0]
    zeta_vals = sol.y[3]

    # Plot trajectory
    plt.plot(zeta_vals, u_vals, lw=1.2, color='blue')

    # Add arrow at appropriate position
    if i < 5:  # For upper trajectories
        arrow_pos = int(len(zeta_vals) * 0.6)
    else:  # For bottom trajectories
        arrow_pos = int(len(zeta_vals) * 0.7)

    if arrow_pos < len(zeta_vals) - 1:
        ax.annotate(
            '',
            xy=(zeta_vals[arrow_pos + 1], u_vals[arrow_pos + 1]),
            xytext=(zeta_vals[arrow_pos], u_vals[arrow_pos]),
            arrowprops=dict(
                arrowstyle='->',
                lw=1,
                mutation_scale=10,
                shrinkA=0, shrinkB=0,
                color='blue'
            ),
        )

# Add Wilson-Fisher label
plt.text(0.02, 24.5, 'Wilson-', fontsize=22, color='red', weight='bold')
plt.text(0.02, 22.8, 'Fisher', fontsize=22, color='red', weight='bold')

# Add fixed point markers
# plt.scatter([0], [0], s=80, color='red', zorder=5, marker='o')  # Gaussian fixed point at origin

# Add separatrix (green dashed line)
separatrix_zeta = np.array([0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68])
separatrix_u = np.array([0, 2.5, 6, 10.5, 16, 22, 28, 34, 40])
plt.plot(separatrix_zeta, separatrix_u, linestyle='--', color='green', linewidth=1.8)

# Add vertical line at critical zeta
plt.axvline(0.517, color='darkorange', linestyle='-.', linewidth=2)

# Set plot limits and labels
plt.xlim(0, 2)
plt.ylim(-0.3, 30)
plt.xlabel(r'$\overline{\zeta}$', fontsize=25)
plt.ylabel(r'$\overline{u}$', fontsize=25)

# Customize axes
for axis in ['bottom', 'left', 'right', 'top']:
    ax.spines[axis].set_linewidth(2.5)
ax.tick_params(axis='both', which='major', labelsize=20, width=2.5, length=7)
ax.tick_params(axis='both', which='minor', width=2.5, length=3.5)

plt.tight_layout()
# plt.savefig('/home/claude/rg_flow_aligned.png', dpi=600, bbox_inches='tight')
plt.show()