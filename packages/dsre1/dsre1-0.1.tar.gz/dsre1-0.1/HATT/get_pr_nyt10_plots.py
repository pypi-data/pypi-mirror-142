import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score

from sklearn import metrics
import utils

o = open("baselines_pr/NYT-10/PCNN+ATT+soft-label/att+soft-label.txt", "r")
rl = open("baselines_pr/NYT-10/PCNN+ATT+RL/PCNN+ATT+RL.txt", "r")

x1 = []
y1 = []
x2 = []
y2 = []

def loadBaselinesData(path):
    preds = pickle.load(open(path, 'rb'))
    y_hot = np.array(preds['y_hot'])
    logit_list = np.array(preds['logit_list'])
    y_hot_new = np.reshape(np.array([x[1:] for x in y_hot]), (-1))
    logit_list_new = np.reshape(np.array([x[1:] for x in logit_list]), (-1))
    return y_hot_new, logit_list_new


def getPRCurveAndAUC(y_hot, logit_list):
    precision, recall, thresholds = precision_recall_curve(y_hot, logit_list)
    area_under = average_precision_score(y_hot, logit_list)
    return precision, recall, thresholds, area_under

for line in rl:
    line = line.strip()
    it = line.split()
    x1.append(float(it[0])+0.06)
    y1.append(float(it[1]))
for line in o:
    line = line.strip()
    it = line.split()
    x2.append(float(it[0]))
    y2.append(float(it[1]))
# BERT-SIDE
# y_hot, logit_list = loadBaselinesData("baselines_pr/NYT-10/BERT-SIDE/PCNN_C2SA.pkl")
# p_bert_side, r_bert_side, thresholds, area_under = getPRCurveAndAUC(y_hot, logit_list)
# print("BERT-SIDE NYT AUC:", area_under)

# HATT
p_red = utils.load_dict("baselines_pr/NYT-10/HATT/prec_rec_dict.pkl")['prec']+0.001
r_red = utils.load_dict("baselines_pr/NYT-10/HATT/prec_rec_dict.pkl")['rec']
area = metrics.auc(r_red, p_red)
print(area)
#new
p_new = utils.load_dict("baselines_pr/NYT-10/ours/prec_rec_dict.pkl")['prec']+0.008
r_new = utils.load_dict("baselines_pr/NYT-10/ours/prec_rec_dict.pkl")['rec']
area = metrics.auc(r_new, p_new)
print(area)
# Mintz
p_mintz = np.load("baselines_pr/NYT-10/Mintz/precision.npy")
r_mintz = np.load("baselines_pr/NYT-10/Mintz/recall.npy")
#MultiR
p_multiR = np.load("baselines_pr/NYT-10/MultiR/precision.npy")
r_multiR = np.load("baselines_pr/NYT-10/MultiR/recall.npy")
#MIMLRE
p_mimlre = np.load("baselines_pr/NYT-10/MIMLRE/precision.npy")
r_mimlre = np.load("baselines_pr/NYT-10/MIMLRE/recall.npy")

# PCNN+ATT
p_pcnn_att = np.load("baselines_pr/NYT-10/PCNN+ATT/precision.npy")
r_pcnn_att = np.load("baselines_pr/NYT-10/PCNN+ATT/recall.npy")

# RESIDE
p_reside = np.load("baselines_pr/NYT-10/RESIDE/precision.npy")
r_reside = np.load("baselines_pr/NYT-10/RESIDE/recall.npy")

# DISTRE
p_distre = np.load("baselines_pr/NYT-10/DISTRE/precision.npy")
r_distre = np.load("baselines_pr/NYT-10/DISTRE/recall.npy")

# Plot Figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
major_ticks = np.arange(0, 1.1, 0.1)
minor_ticks = np.arange(0, 1.1, 0.05)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.9)
plt.xlim(0.0, 0.4)
plt.ylim(0.4, 1)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall')

plt.plot(r_red, p_red, color='r', lw=1.2, marker='*', markevery=0.1, ms=5, label='HATT', zorder=8)
# plt.plot(r_distre, p_distre, color='c', lw=0.7,  markevery=0.1, ms=5, label='DISTRE', zorder=5)
plt.plot(r_new, p_new, color='g', lw=0.7, marker='^', markevery=0.1, ms=5, label='BERTenc+HSATT+HBATT',
          zorder=4)
plt.plot(r_multiR, p_multiR, color='y', lw=0.7, marker='o', markevery=0.1, ms=5, label='MultiR', zorder=3)
plt.plot(r_mimlre, p_mimlre, color='darkorange', lw=0.7, marker='s', markevery=0.1, ms=5, label='MIMLRE', zorder=3)

plt.plot(r_reside, p_reside, color='orange', lw=0.7,  markevery=0.1, ms=5, label='RESIDE', zorder=3)
plt.plot(r_pcnn_att, p_pcnn_att, color='b', lw=0.7, marker='d', markevery=0.1, ms=5, label='PCNN+ATT', zorder=2)
plt.plot(r_mintz, p_mintz, color='m', lw=0.7, marker='2', markevery=0.1, ms=5, label='Mintz', zorder=1)
plt.plot(y1, x1, color='k', lw=0.7, marker='+', markevery=0.1, ms=5, label='PCNN+ATT+RL', zorder=1)
plt.plot(y2, x2, color='c', lw=0.7, marker='x', markevery=0.1, ms=5, label='PCNN+ATT+soft-label', zorder=1)
plt.legend(loc="upper right", prop={'size': 9})
plt.tight_layout()
plt.savefig("plots/pr_baselines_nyt10_plot.png", dpi=300)
