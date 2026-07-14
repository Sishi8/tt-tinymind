# TinyMind – A Tiny AI Inference Accelerator

TinyMind is a miniature AI inference accelerator implemented entirely in digital hardware.

Instead of running software, this chip contains three simple artificial neurons built directly from logic gates.

The goal of the project is to demonstrate one of the most important ideas behind modern AI hardware:

> **Training happens before fabrication. Inference happens on the chip.**

---

# Vocabulary

Before trying the project, here are a few important words.

## Artificial Neuron

An artificial neuron is a small mathematical model inspired by neurons in the human brain.

It receives several inputs, combines them using a set of weights, and produces a score.

The neuron with the highest score "wins."

---

## Feature

A feature is simply one piece of information given to the AI.

In TinyMind, every input switch represents one feature.

For example:

- Likes mathematics
- Likes programming
- Likes electronics
- Likes physics
- Likes data and patterns
- Likes building things
- Likes creativity
- Likes experimentation and research

Each feature is either:

- **0** → No
- **1** → Yes

---

## Weight

A weight tells the neuron how important a feature is.

TinyMind uses **ternary weights**, meaning every weight is one of only three values.

| Weight | Meaning |
|---------|----------|
| +1 | This feature supports the class |
| 0 | Ignore this feature |
| -1 | This feature works against the class |

For example, if an AI-oriented neuron thinks mathematics is important, it might assign:

```
Math → +1
```

If it thinks electronics are not important, it might assign:

```
Electronics → 0
```

If it thinks building things makes the prediction less likely, it might assign:

```
Building → -1
```

---

## Training

Training is the process of learning the best weights.

Normally this happens on a computer or GPU using many examples.

TinyMind **does not perform training.**

Its weights are permanently built into the hardware.

---

## Inference

Inference means making a prediction using already-learned weights.

This is exactly what TinyMind does.

Every time the switches change, the chip immediately performs a new prediction.

---

# How TinyMind Works

TinyMind contains **three artificial neurons** running in parallel.

Each neuron represents one possible class.

```
              Eight Input Features
                      │
                      ▼
         ┌────────────────────────┐
         │   AI Neuron            │
         └────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │ Hardware Neuron        │
         └────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │ Creative Neuron        │
         └────────────────────────┘
                      │
                      ▼
            Compare the three scores
                      │
                      ▼
            Highest score wins
```

Each neuron calculates a score using its own fixed weights.

The neuron with the highest score becomes the prediction.

---

# Display

The Tiny Tapeout demonstration board has only a single seven-segment display.

TinyMind alternates between two views whenever the step clock is pressed.

## View 1 – Predicted Class

The display shows:

| Display | Meaning |
|----------|----------|
| A | AI-oriented |
| H | Hardware-oriented |
| C | Creative-oriented |

If the decimal point is illuminated, the prediction was very close.

---

## View 2 – Confidence Margin

The display shows a digit from **0–9**.

This is calculated as:

```
Winning Score − Second Highest Score
```

A larger number means the AI made a stronger decision.

A smaller number means two classes produced similar scores.

---

# Example

Suppose the switches are:

| Feature | Value |
|----------|------|
| Mathematics | Yes |
| Programming | Yes |
| Electronics | No |
| Physics | No |
| Data | Yes |
| Building | No |
| Creativity | No |
| Research | Yes |

Internally, the three neurons might calculate:

| Class | Score |
|--------|------:|
| AI | **5** |
| Hardware | 2 |
| Creative | 1 |

The display first shows:

```
A
```

Press the step clock once.

The display changes to:

```
3
```

This means the AI class won by three points.

---

# Why This Is an AI Accelerator

Modern AI accelerators perform large numbers of neural-network calculations in dedicated hardware.

TinyMind demonstrates the exact same idea on a much smaller scale.

Instead of billions of neurons, TinyMind contains three.

Instead of millions of weights, TinyMind contains a handful of fixed ternary weights.

Although extremely small, it illustrates the same fundamental inference process used by modern AI hardware.

---

# How to Test

1. Move any combination of the eight input switches.
2. Observe the predicted class on the seven-segment display.
3. Press the step clock.
4. Observe the confidence margin.
5. Continue experimenting with different feature combinations.

Notice how changing only one feature can sometimes change the prediction.

---

# External Hardware

This project uses only the standard Tiny Tapeout demonstration board.

No additional external hardware is required.
