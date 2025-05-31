from openai import OpenAI

client = OpenAI()

themes = [
    "Speed = distance / time",
    "Acceleration = change in velocity / time",
    "Newton's First Law of Motion",
    "Newton's Second Law (F = ma)",
    "Newton's Third Law of Motion",
    "Weight = mass × gravitational field strength",
    "Mass vs. weight",
    "Kinetic energy = 0.5 × mass × velocity^2",
    "Potential energy = mass × gravity × height",
    "Conservation of energy",
    "Power = work / time",
    "Work = force × distance",
    "Gravitational potential energy",
    "Hooke’s Law (F = kx)",
    "Elastic potential energy",
    "Friction force",
    "Normal force",
    "Air resistance",
    "Terminal velocity",
    "Momentum = mass × velocity",
    "Conservation of momentum",
    "Impulse = force × time",
    "Free fall motion",
    "Projectile motion",
    "Distance-time graph interpretation",
    "Velocity-time graph interpretation",
    "Area under velocity-time graph = displacement",
    "Slope of distance-time graph = speed",
    "Slope of velocity-time graph = acceleration",
    "Thermal expansion of solids",
    "Conduction of heat",
    "Convection of heat",
    "Radiation of heat",
    "Specific heat capacity",
    "Latent heat of fusion",
    "Latent heat of vaporization",
    "States of matter and particle theory",
    "Pressure = force / area",
    "Atmospheric pressure",
    "Pressure in liquids = density × gravity × height",
    "Buoyant force (Archimedes' principle)",
    "Pascal’s Principle",
    "Bernoulli’s Principle (basic idea)",
    "Simple harmonic motion (spring or pendulum basics)",
    "Wave speed = frequency × wavelength",
    "Reflection of light",
    "Refraction of light",
    "Snell's Law (qualitative)",
    "Dispersion of light",
    "Laws of reflection",
    "Total internal reflection",
    "Plane mirror image characteristics",
    "Concave mirror ray diagrams",
    "Convex mirror ray diagrams",
    "Lenses (concave and convex, basic behavior)",
    "Light travels in straight lines",
    "Color and visible spectrum",
    "Sound travels as longitudinal wave",
    "Speed of sound in air",
    "Echo and reflection of sound",
    "Frequency and pitch of sound",
    "Amplitude and loudness of sound",
    "Electrostatics: charges attract/repel",
    "Charging by friction",
    "Conductors vs. insulators",
    "Electric current = charge / time",
    "Voltage = energy / charge",
    "Ohm’s Law (V = IR)",
    "Resistance = voltage / current",
    "Series circuit: total resistance",
    "Parallel circuit: current splitting",
    "Series circuit: voltage division",
    "Electric power = voltage × current",
    "Electric energy = power × time",
    "Magnetic fields around magnets",
    "Magnetic field around current-carrying wire",
    "Right-hand rule for current and magnetic field",
    "Electromagnets",
    "Factors affecting strength of electromagnet",
    "Simple electric motor (basic principle)",
    "Electromagnetic induction (basic concept)",
    "Static electricity and sparks",
    "Earth’s magnetic field",
    "Compass and magnetic poles",
    "Gravitational field strength on Earth",
    "Mass of Earth (known constant)",
    "Density = mass / volume",
    "Units of force (newton)",
    "Units of pressure (pascal)",
    "Units of energy (joule)",
    "Units of power (watt)",
    "Conversion between energy units (kWh to J)",
    "Speed of light in vacuum",
    "Law of conservation of mass",
    "Simple lever principle",
    "Moment = force × perpendicular distance",
    "Equilibrium of moments",
    "Center of mass",
    "Stability and base of support",
    "Pulleys (mechanical advantage basics)",
    "Inclined plane mechanics",
    "Simple machines: efficiency = useful energy out / total energy in"
]

prompt_template = """You are a physics tutor tasked with generating high-quality, diverse numerical word problems for fine-tuning a model.

Theme: **{theme}**

Your task:
1. Generate 10 unique, word problems 
2. The problems should be within a range of difficulty from 3rd grade to 10th grade level.
3. Ensure that each problem is solvable using only the provided information.
4. For each problem, include the following:
   - A problem statement in plain English.
   - A brief reasoning explanation (1–3 sentences) showing the key steps or approach to solving the problem.
   - The final answer, expressed as a single, accurate numerical value with correct units (e.g., "48 J", "12.5 m/s").
   - Vary the phrasing, context, and complexity across the problems to avoid repetition.
5. Determining whether an answer is correct can be ambiguous. To address this, provide a list of approximately five acceptable answers in the `"solutions"` field for each problem — for example: ["12J", "12.0 J", "12 Joules", "12 joules"].
6. Once you have generated the problems, and their solutions, format them as a JSON Lines file with the following structure:
   ```json
   {{"question": "A car accelerates at 3.2 m/s² for 5 seconds. What is its final velocity?", "solutions": ["16 m/s", "16.0 m/s", "16 ms⁻¹", "16.0m/s", "16 meters per second"]}}
   {{"question": "A 2 kg object is lifted 10 meters. What is its gravitational potential energy?", "solutions": ["196 J", "196.0 J", "196 Joules", "196 joules", "196J"]}}
   ...
   ```
"""

for theme in themes:
    response = client.responses.create(model="gpt-4o", input=prompt_template.format(theme=theme))
    print(response.output_text)
