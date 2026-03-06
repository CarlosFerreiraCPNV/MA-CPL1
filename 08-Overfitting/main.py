import math
import random

# -------------------------
# Données (TP Overfitting)
# -------------------------
TRAIN = [
    # y = 1 (x2 haut)
    (0.2, 4.8, 1), (0.6, 4.4, 1), (1.0, 4.9, 1), (1.3, 4.2, 1),
    (1.7, 4.6, 1), (2.0, 4.7, 1), (2.4, 4.3, 1), (2.8, 4.9, 1),
    (3.1, 4.4, 1), (3.5, 4.8, 1), (3.9, 4.2, 1), (4.3, 4.6, 1),
    (4.7, 4.9, 1), (4.9, 4.3, 1),

    # y = 0 (x2 bas)
    (0.1, 0.3, 0), (0.4, 0.8, 0), (0.9, 0.5, 0), (1.2, 1.0, 0),
    (1.6, 0.2, 0), (2.1, 0.7, 0), (2.5, 0.4, 0), (2.9, 1.1, 0),
    (3.2, 0.6, 0), (3.6, 0.9, 0), (4.0, 0.3, 0), (4.4, 1.0, 0),
    (4.8, 0.5, 0),

    # quelques contre-exemples (bruit) pour éviter un dataset "trop parfait"
    (4.6, 4.7, 0),  # bruit: x2 haut mais y=0
    (0.5, 0.4, 1),  # bruit: x2 bas mais y=1
    (3.8, 0.6, 1),  # bruit: x2 bas mais y=1
    (1.1, 4.5, 0),  # bruit: x2 haut mais y=0
]

VAL = [
    # y = 1 (x1 haut, x2 varié)
    (4.6, 0.4, 1), (4.2, 4.8, 1), (4.9, 1.1, 1), (4.4, 3.9, 1),
    (3.9, 0.7, 1), (4.7, 2.6, 1), (4.1, 1.9, 1), (4.8, 4.2, 1),
    (3.8, 3.1, 1), (4.3, 0.9, 1), (4.0, 2.2, 1), (4.5, 1.4, 1),

    # y = 0 (x1 bas, x2 varié)
    (0.4, 4.7, 0), (0.9, 0.6, 0), (1.1, 4.9, 0), (1.5, 1.0, 0),
    (2.0, 4.6, 0), (2.2, 0.4, 0), (1.8, 3.8, 0), (0.7, 2.5, 0),
    (2.4, 4.2, 0), (1.3, 0.8, 0), (0.2, 3.1, 0), (2.1, 1.9, 0),
]

ETA = 0.1
EPOCHS = 200

# -------------------------
# Modèle : neurone logistique
# z = w1*x1 + w2*x2 + b
# p = sigmoid(z)
# -------------------------

def sigmoid(z: float) -> float:
    # petite sécurité numérique pour éviter exp overflow
    if z < -60:
        return 0.0
    if z > 60:
        return 1.0
    return 1.0 / (1.0 + math.exp(-z))

def predict_proba(x1: float, x2: float, w1: float, w2: float, b: float) -> float:
    z = w1 * x1 + w2 * x2 + b
    return sigmoid(z)

def predict(x1: float, x2: float, w1: float, w2: float, b: float) -> int:
    return 1 if predict_proba(x1, x2, w1, w2, b) >= 0.5 else 0

def bce_loss(y: int, p: float) -> float:
    # Binary Cross-Entropy : -[ y log(p) + (1-y) log(1-p) ]
    eps = 1e-12
    p = min(max(p, eps), 1.0 - eps)
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))

def accuracy(data, w1: float, w2: float, b: float) -> float:
    correct = 0
    for x1, x2, y in data:
        y_pred = predict(x1, x2, w1, w2, b)
        if y_pred == y:
            correct += 1
    return correct / len(data)

def train():
    # init poids (petits nombres aléatoires)
    w1 = random.uniform(-0.5, 0.5)
    w2 = random.uniform(-0.5, 0.5)
    b = random.uniform(-0.5, 0.5)

    for epoch in range(1, EPOCHS + 1):
        total_loss = 0.0

        # 1 epoch = passer sur tout TRAIN
        for x1, x2, y in TRAIN:
            # forward
            z = w1 * x1 + w2 * x2 + b
            p = sigmoid(z)
            total_loss += bce_loss(y, p)

            # gradient (logistic regression)
            # dL/dz = (p - y)
            dz = (p - y)
            dw1 = dz * x1
            dw2 = dz * x2
            db  = dz

            # update (descente de gradient)
            w1 -= ETA * dw1
            w2 -= ETA * dw2
            b  -= ETA * db

        train_acc = accuracy(TRAIN, w1, w2, b)
        val_acc = accuracy(VAL, w1, w2, b)

        print(f"Epoch {epoch:3d} | Loss: {total_loss:.4f} | Train: {train_acc:.2%} | Val: {val_acc:.2%}")

    print("\nPoids finaux :")
    print(f"w1={w1:.4f}, w2={w2:.4f}, b={b:.4f}")

if __name__ == "__main__":
    train()
