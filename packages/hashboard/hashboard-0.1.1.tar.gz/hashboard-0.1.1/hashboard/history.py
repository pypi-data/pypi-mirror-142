
import numpy as np
import pandas as pd

# Mean and standard deviation of the logarithm of the sum of 48
# independent identically distributed exponential random variables
# (known as ExpGammaDistribution[48,1,0] in Wolfram Mathematica).
eg48_mean = 3.8607481768292526
eg48_std = 0.14509257090677763

# We have log(duration) = log(2) * zero_bits + X - log(hashrate),
# where X is an ExpGammaDistribution[48,1,0] random variable and
# duration is the length of a phase (the interval between the
# (48n)th and (48(n+1))th blocks being mined).


def expand_history(df):
    '''
    Compute derived statistics from a history dataframe:
    '''

    df = df.copy()
    df['duration'] = df['end_time'] - df['start_time']
    df['log_fees'] = np.log(df['fees_btc'])
    df['log_reward'] = np.log(df['fees_btc'] + df['subsidy_btc'])
    df['log_price'] = np.log(df['price'])

    # Compute an unbiased (mean-zero) estimator of log(hashrate)
    # by reverse-engineering the formula for log(duration). This
    # estimator is called ilhr ('instantaneous log hashrate') and
    # has a standard deviation of eg48_std from true log(hashrate).
    df['ilhr'] = np.log(2) * df['zero_bits'] + eg48_mean - np.log(df['duration'])

    return df


def download_csv(csvname):

    print('Downloading CSV "%s" from Hatsya...' % csvname)
    df = pd.read_csv("https://catagolue.hatsya.com/textsamples/xs0_%s/b3s23/synthesis" % csvname)
    return df


def phase_to_subsidy(x):

    return 1.0e-8 * (5000000000 >> (x // 4375))


def download_history():

    df = download_csv('phases')

    subsidy_btc = df['phase'].apply(phase_to_subsidy)
    reward_btc = df['total_reward'] / 48e8

    # We ensure that fees are positive so that we can take the logarithm.
    # (Fees could be negative in practice if miners fail to claim the whole
    # block reward.) A lower bound of 1000 sats per block is conservative,
    # because the average number of transactions in a full block is >= 1000
    # and it is inconceivable that fees will drop below 1 sat per transaction
    # (that would equate to free transactions, since sats are indivisible!).
    fees_btc = np.maximum(0.00001000, reward_btc - subsidy_btc)

    cols = {'phase': df['phase'],
            'start_time': df['start_time'],
            'end_time': df['end_time'],
            'zero_bits': df['zero_bits'],
            'fees_btc': fees_btc,
            'subsidy_btc': subsidy_btc,
            'price': 1e8 * df['total_reward_usd'] / df['total_reward']}

    df = pd.DataFrame(cols)
    assert np.all(df['phase'] == df.index)
    print('Downloaded history up to block height %d' % (48 * len(df)))

    # Include derived statistics:
    df = expand_history(df)

    return df
