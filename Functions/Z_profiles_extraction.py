import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def extract_Z_profiles(stack):
    # stack is [t, Z, x, y] shape so we operate a mean over X and Y
    profiles = np.mean(stack, axis=(2, 3))
    print(f"Extracted profiles shape: {profiles.shape}")
    return profiles

def plot_profiles(profiles):
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))

    cmap = plt.cm.viridis
    norm = colors.Normalize(vmin=0, vmax=(profiles.shape[1] - 1))  # Normalize to Z range
    
    for i in range(profiles.shape[1]):
        axes[0].plot(np.arange(profiles.shape[0]) * 5 / 60, profiles[:, i], color=cmap(norm(i)))
    axes[0].set_xlabel('Time [h]')
    axes[0].set_ylabel('Intensity')
    axes[0].set_title('Profiles Over Time and Z')

    mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    mappable.set_array([])
    cbar = fig.colorbar(mappable, ax=axes[0])
    cbar.set_label('Z [µm]')
    z_ticks = np.arange(0, profiles.shape[1], max(1, profiles.shape[1]//5))
    cbar.set_ticks(z_ticks)
    cbar.set_ticklabels([f'{z*0.5:.1f}' for z in z_ticks])
    

    axes[1] = plt.subplot(122, projection='3d')
    T, Z = np.meshgrid(np.arange(profiles.shape[0])*5/60, np.arange(profiles.shape[1])*0.5)
    axes[1].plot_surface(Z, T, profiles.T, cmap='viridis')
    axes[1].set_xlabel('Z [µm]')
    axes[1].set_ylabel('Time [h]')
    axes[1].set_zlabel('Intensity')
    axes[1].set_title('3D Surface Plot of Profiles')
    plt.tight_layout()
    plt.show()

"""
from scipy import stats

def estimate_sigma2(Z):
    
    diffs = np.diff(Z)
    return np.sum(diffs**2) / (2 * (len(Z) - 1))

def test_L2(Z1, Z2):

    N = len(Z1)
    D = Z1 - Z2
    S = np.sum(D**2)
    
    sigma2 = (estimate_sigma2(Z1) + estimate_sigma2(Z2)) / 2
    T = S / (2 * sigma2)
    
    p_value = 1 - stats.chi2.cdf(T, df=N)
    chi2_threshold = stats.chi2.ppf(0.95, df=N)
    
    return {
        "T": T,
        "chi2_seuil_95": chi2_threshold,  # ≈ 264 pour N=229
        "p_value": p_value,
        "rejet_H0": T > chi2_threshold
    }

stack = np.load('/run/media/kontowicz/TEDDY/Data_Tokyo/20251001/bacteria-image_binerizer/Functions/stack_fluo_bin.npy')


profiles = extract_Z_profiles(stack)
plot_profiles(profiles)

A = test_L2(profiles[:, 0], profiles[:, 5])
print(f"Test L2 Results: {A}")


#plt.figure()
#plt.plot(D_bar, label='D_bar')
#plt.xlabel('Time')
#plt.ylabel('D_bar Intensity')
#plt.title('D_bar Over Time')
#plt.legend()
#plt.show()
"""