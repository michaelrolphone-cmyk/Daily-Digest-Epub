# Daily Digest — October 17, 2026 · Technical Discovery

Light–sound coupling, parallel silicon qubits, molecular spins, mobile traps and ESP32 radio experiments

Reporting cutoff: 2026-10-17T01:50:00-06:00 (America/Boise)

This edition explains six experimentally grounded topics: fiber light–sound hybrid modes, crosstalk correction for five parallel spin qubits, odd-even molecular boundary states, ions stored during road transport, and two ESP32 projects exposing unexpected uses of radio hardware. Published journal results, preprints, original code and community claims are distinguished. All essential details are readable offline.

## Physics / Optoacoustics / Research Feature — Light and sound form hybrid modes without a cavity

A single-pass fiber experiment measures a split resonance and an avoided crossing by manipulating Brillouin detuning.

Blázquez Martínez, Zhu and Stiller, Nature Physics, October 16, 2026, DOI 10.1038/s41567-026-03458-2; preprint arXiv:2507.08673 from 2025, revised August 24, 2026.

Strong coupling normally means holding interacting systems near one another long enough to exchange energy before they lose coherence. Optical cavities accomplish this by storing light for many trips, but impose narrow frequency windows and demanding tuning. On October 16, Nature Physics published an experiment by Laura Blázquez Martínez, Changlong Zhu and Birgit Stiller reaching optoacoustic strong coupling in a single pass through nonlinear optical fiber. The study's central observation is not simply more Brillouin gain: a traveling light field and traveling sound modes form spectrally distinct hybrid modes despite the absence of a cavity. [1]

The process is anti-Stokes Brillouin–Mandelstam scattering. A strong optical pump interacts with an acoustic density wave and produces higher-frequency scattered light while removing a phonon. The waveguide has an almost continuous range of acoustic wave numbers, but optical momentum conservation selects those that are phase matched. The Brillouin frequency is about 9.5997 GHz in this sample. A coupled-oscillator picture has interaction H_int = hbar*g*(a†b+b†a), where a and b represent optical and acoustic modes, dagger means creation, and g is the pump-enhanced coupling. The exchange terms mix modes; spectral splitting becomes resolvable when coupling wins against loss. [2]

The group used germanium-enriched nonlinear fiber in a cryostat near 4 K, pumped around 1550 nanometers. Cooling changed two experimentally measured material properties at once. The Brillouin gain increased from 1.60 ± 0.06 inverse-watt inverse-meter at 293 K to 6 ± 1 at 4 K, while the acoustic damping rate fell from 46.3 ± 0.2 to 9.91 ± 0.07 MHz. Effective optical dissipation was 24 ± 2 MHz and the fiber's optical propagation loss was 0.001 dB per meter. This combination matters because a powerful pump does not reveal clean hybrid modes when acoustic oscillations lose energy too rapidly. [1] [2]

At weak drive the fitted coupling was g=13 ± 2 MHz and the optical response resembled one Lorentzian peak. With more pump power the peak split; at g=71 ± 2 MHz the maximum experimentally observed peak separation was 26.7 MHz. Treating the coupling parameter as a directly measured peak spacing would be an error. In the continuum model g characterizes the interaction, whereas the spacing comes from a dissipative, propagation-dependent spectral measurement. The team compared spectral shapes with the theoretical model at varied pump powers, and that agreement supports the hybrid-mode interpretation rather than a trivial pump-induced gain change. [1] [2]

The second technique is particularly instructive. In a cavity, one can detune the mechanical and optical resonances and see an avoided crossing: the two eigenfrequencies repel. In a fiber, sweeping the optical probe normally selects a correspondingly different phase-matched acoustic mode, so conventional Brillouin spectroscopy can remain effectively resonant. The team created a forced-detuning map by splitting a laser into pump, probe and local oscillator, shifting the probe electro-optically and detecting the scattered response with heterodyne electronics. With pump power 1.35 ± 0.1 watt and probe power 0.6 microwatt, the spectrum at g=64 ± 2 MHz showed mode repulsion absent from a weak-coupling control. [1] [2]

The resolved split and avoided-crossing pattern are complementary evidence. They show the optical and acoustic components hybridize and exchange their character as the drive is detuned. They do not demonstrate a quantum memory, entanglement, or faithful conversion of an unknown single-photon state. A thermal acoustic bath remains populated at four kelvin. The authors indicate that greater pump strength, perhaps several watts in their model, or a lower-loss material is needed for a genuinely quantum-coherent transfer regime. Their actual result is strong classical coupling with a path toward, but not completion of, low-noise quantum operation. [1] [2]

**Analysis.** For a scale calculation, a 9.5997-GHz mechanical oscillation has a period T=1/f of roughly 104 picoseconds. The equilibrium Bose–Einstein occupation formula n=1/[exp(h*f/(k_B*T_kelvin))−1], with Planck's constant h and Boltzmann's constant k_B, gives about eight thermal phonons at 4 K. This is our derived equilibrium estimate, not a number measured by the experiment. It shows why simply attaining a narrow, resolved hybrid-mode spectrum does not automatically imply nearly noise-free acoustic excitation. The acoustic frequency is high, but the sample is not in its ground state. [1] [2]

The transferable engineering principle is replacing resonant recirculation with a high-gain, low-loss, phase-matched interaction occurring during propagation. Standard-fiber splicing and telecommunications wavelengths could make this useful for distributed photonic signal processing, but cryogenic hardware and appreciable optical pump power remain limitations. Chronology also matters: this result was available in an older arXiv preprint, updated August 24, 2026. October 16 is the journal publication date, not the first moment the underlying work became public. [1] [2]

### Sources

1. [Nature Physics — Cavity-less Brillouin strong coupling in a solid-state continuous system](https://www.nature.com/articles/s41567-026-03458-2) — 2026-10-16.

2. [Blázquez Martínez et al. / arXiv — Full experiment and theory, arXiv:2507.08673](https://arxiv.org/html/2507.08673) — 2026-08-24.

## Physics / Quantum Hardware — Five silicon spins, one microwave line, and a fix for parallel crosstalk

The leading error is a spectator phase shift that pairwise calibration can compensate without exhaustively testing every concurrent drive pattern.

Wu, Camenzind, Bütler et al.; Nature Physics DOI 10.1038/s41567-026-03466-2, published October 15, 2026; older preprint arXiv:2507.11918.

A silicon spin qubit can be extremely accurate when addressed by itself yet fail when its neighbors receive gates concurrently. Quantum error-correction circuits need parallel steps because an idle qubit keeps dephasing while a controller serializes instructions. In their October 15 Nature Physics paper, Yi-Hsien Wu, Leon Camenzind and collaborators quantify this problem and show a strategy for sharing one microwave electrode across five spin qubits. Their device's typical idle dephasing time is about ten microseconds, whereas coherence under continuous drive is about one hundred microseconds. That gap makes efficient concurrent control an architectural requirement rather than a mere optimization. [1]

The five quantum dots are defined in an isotopically enriched silicon-28 quantum well within silicon-germanium. Electrostatic gates position electrons and tune their interactions; a cobalt micromagnet supplies a field gradient. An applied microwave electric field moves electron wavefunctions in that gradient, rotating the spin by electric-dipole spin resonance. Neighboring resonance frequencies are separated by approximately 150 MHz, so tones can address different dots even though they share a microwave line. Charge sensors and spin-blockade procedures establish initial states and read them out. The operating environment remains cryogenic and carefully calibrated. [2]

The dominant simultaneous-drive error is not necessarily an unwanted complete spin flip. A microwave tone far from a neighbor's resonance can still shift that neighbor's energy splitting by the AC Stark effect. If the pulse lasts long enough, the spectator spin accumulates an unintended relative phase. In the approximate large-detuning limit, the shift scales with the square of drive amplitude divided by frequency detuning. That relation is illustrative, not a fitted equation for this particular chip. Importantly, a spin population measurement can look benign immediately after a pulse even when its phase error will corrupt subsequent operations. [1] [2]

The authors shaped microwave pulses with a Kaiser window to suppress spectral leakage, then calibrated drive-induced spectator phase effects in pairs. The number of unordered pairs grows as N*(N−1)/2 instead of examining all 2^N combinations of active qubits. With five qubits, that is ten pairs compared with thirty-two activity masks; at fifty, 1,225 pairs versus more than a quadrillion masks. The second comparison is mathematical scaling, not an experimental fifty-spin result. Calibrated phase compensation works because the leading unwanted shifts can be approximated as a combination of measurable pairwise terms. [1] [2]

Randomized benchmarking estimated primitive X and Y rotation fidelity above 99.99% on each isolated qubit, with some around 99.999%. Three qubits operated simultaneously retained fidelities above 99.99%; all five executing together stayed around or above 99.9%. Those percentages refer to the paper's benchmarking model and gate definitions, not a logical computer's crash rate. The corresponding average primitive-gate infidelities are about 0.01% and 0.1%, a factor of ten apart. The reported performance is for parallel single-qubit operations; simultaneous high-fidelity entangling gates and full error-correction cycles were not demonstrated. [1] [2]

**Analysis.** The scientific advance is identifying a tractable phase-calibration problem inside a shared-control architecture. The limitation is equally concrete: when many drives produce nonlinear heating, drift or genuinely higher-order interactions, pairwise correction might not capture all crosstalk. Randomized benchmarking also averages errors that may be correlated in actual error-correction workloads. A shared microwave line reduces cabling but cannot make calibration and microwave isolation free. The study demonstrates a five-qubit solution to a measured control obstacle and suggests a way to scale its calibration burden, without establishing scalable fault tolerance. [1] [2]

### Sources

1. [Nature Physics — Simultaneous high-fidelity single-qubit gates in a spin qubit array](https://www.nature.com/articles/s41567-026-03466-2) — 2026-10-15.

2. [Wu et al. / arXiv — Detailed device and randomized benchmarking, arXiv:2507.11918](https://arxiv.org/abs/2507.11918) — 2026-07-17.

## Physics / Topological Spin Systems — Odd and even spin chains talk differently to a superconductor

Atomically assembled triangulene chains reveal parity-selected magnetic bound states associated with emergent edge spins.

Vaxevani, Ortuzar, Trivini and colleagues, Nature 658, 617–622, published October 14, 2026, DOI 10.1038/s41586-026-11117-y; preprint arXiv:2608.22736.

Integer-spin chains have a surprising low-energy structure. Although each microscopic unit carries spin one, correlations across an antiferromagnetic chain create effective spin-one-half states at its ends. These are boundary excitations of the Haldane phase rather than physically divided electrons. Katerina Vaxevani, Jon Ortuzar and colleagues asked whether the end excitations remain recognizable when a molecular chain interacts with a superconductor. Their Nature paper published October 14 demonstrates a sharp parity effect: changing the number of spin-one building blocks from even to odd changes the appearance of magnetic bound states inside a superconducting gap. [1]

The researchers assembled triangulene molecules behaving as spin-one units, linked antiferromagnetically on a gold film grown over niobium. Gold at this interface inherits superconducting correlations through the proximity effect. A scanning tunneling microscope can identify the chain length and structure; differential tunneling conductance dI/dV reveals energies available to electron-like excitations. That combination is more discriminating than measuring magnetization of a bulk ensemble. Individual chains of different lengths can be characterized under nearly the same superconducting environment, allowing a parity-dependent comparison. [2]

A magnetic moment coupled to a superconductor can produce Yu–Shiba–Rusinov states—bound electronic excitations inside the superconducting energy gap. The gap suppresses ordinary quasiparticle states at low energy, so in-gap peaks are a sensitive indicator of magnetic coupling. In these experiments odd-length spin chains have an effective total-spin S=1 ground state and show YSR features. Even-length chains form an S=0 ground state without that same uncompensated magnetic response. The presence or absence of a peak does not establish a Majorana particle or a usable qubit by itself; the interpretation depends on the complete spectroscopy and model. [1] [2]

The reason for alternation lies in the interaction of the two emergent end spins. In a finite chain, they can couple through the intervening bulk, and the sign of their effective exchange alternates with chain parity. A singlet-like combined state is magnetically quiet, whereas a triplet-like state can couple to the superconducting quasiparticles. The authors model two effective edge spins with a superconducting environment and compare the result against measured tunneling features. They also resolve excitations outside the gap, helping distinguish this explanation from an artifact due only to substrate structure or local defects. [1] [2]

Extended data report even-chain spin excitations near 6.3 millielectronvolts for four triangulene units and 3.1 millielectronvolts for six. These are spectroscopic transition energies, not gate operation powers or electrical energy savings. Their decrease with increasing chain length is consistent with weaker interaction between distant ends. The observation connects two many-body concepts often taught separately: edge states of gapped topological spin chains and impurity-induced electronic bound states in superconductors. Here the molecule's parity changes the collective spin seen by the condensate. [1] [2]

**Analysis.** This remains a controlled cryogenic surface-science experiment. The paper does not report fast electrical switching, logical gate fidelity, initialization overhead, coherence time or readout of a complete molecular qubit. Its value is revealing a tunable coupling mechanism with atomically counted building blocks and corroborating excitations. Future hybrid spin-superconductor devices might exploit it, but they would need to demonstrate coherent manipulation and scalable contacts rather than merely reproduce the spectroscopic parity pattern. The underlying preprint appeared in August; October 14 is the date of the published peer-reviewed article. [1] [2]

### Sources

1. [Nature — Parity-dependent coupling of molecular spin chains to a superconductor](https://www.nature.com/articles/s41586-026-11117-y) — 2026-10-14.

2. [Vaxevani et al. / arXiv — Full molecular spectroscopy and spin model, arXiv:2608.22736](https://arxiv.org/abs/2608.22736) — 2026-08-24.

## Physics / Atomic Instruments / Preprint — Thousands of ions survived a 63-kilometer drive in a Paul trap

A moving laboratory stored particles for 15 and 45 minutes; destructive counts do not imply coherent quantum operations during travel.

Alfaro and colleagues, experimental arXiv preprint 2610.20487 posted October 14, 2026; not described as peer-reviewed.

Trapped-ion processors usually occupy quiet laboratory installations with stable vacuum, RF supplies and aligned optics. Before asking whether a quantum node could function during transport, there is a simpler physical question: can ions remain confined while their apparatus rides over roads? An October 14 preprint by Alfaro and collaborators reports operating a linear radio-frequency Paul trap in a moving van and detecting ions after transport. This is evidence for mobile particle storage. It must not be confused with preserving a coherent qubit, executing a gate on the highway or distributing entanglement to another vehicle. [1]

A Paul trap overcomes the impossibility of stable three-dimensional confinement with purely static electrostatics by using a rapidly oscillating quadrupole field. Charged particles perform fast micromotion around a slower secular trajectory in an effective pseudopotential. The researchers describe four electrodes about 1.75 millimeters in radius and 40 millimeters long, powered near 17.1 MHz with RF amplitude around 600 volts. DC endcaps at roughly one kilovolt limit longitudinal motion. The exact stable region depends on charge-to-mass ratio, drive frequency, electrode geometry and perturbations; the field does not immobilize particles as if fixed in a mechanical cage. [1]

The van contained vacuum equipment maintaining pressure better than approximately 3×10^-11 millibar and protected power supplies. Laser ablation loaded positive particles whose mass-to-charge ratio was approximately twelve atomic mass units per elementary charge, consistent mainly with carbon ions. An extraction pulse sent the stored cloud to a microchannel-plate detector after the journey. This method measures remaining population destructively, rather than continuously observing individual particle trajectories. The ions were not laser cooled and coherently manipulated as qubits during the road test. [1]

One run traveled 18.6 kilometers; after fifteen minutes the authors estimated 3.82(6)(1.3)×10^3 stored ions, or about 3,820 with uncertainties of roughly 60 statistical and 1,300 systematic. Another traveled 63.4 kilometers and ended after forty-five minutes with 1.17(3)(3.9)×10^3 ions, about 1,170 with uncertainties near 30 and 390. Different initial clouds were loaded for the separate trips. Their counts cannot be treated as two successive time points of the same single population, even though the lower number on the longer trip is consistent with ordinary storage loss. [1]

A simple survival model has N(t)=N0 exp(−t/τ), where τ is the fitted lifetime. The paper reports stationary τ near 2.6(5)×10^3 seconds and moving τ near 1.52(71)×10^3 seconds. The substantial uncertainty prevents precise attribution of a mobility-induced extra loss rate. The editorial calculation exp(−1800/1520)≈0.31 predicts a rough survival factor over half an hour at the nominal moving lifetime; it is not another measurement and does not establish that road vibration killed 69% of ions. Gas collisions, pressure, power stability and mechanical effects can interact. [1]

**Analysis.** The experiment demonstrates a prerequisite for mobile trapped-ion hardware: a powered RF trap can retain thousands of charged particles over meaningful road travel. The remaining science is formidable. Optical alignment, laser cooling, motional heating measurement, control of internal electronic states, gate fidelity and quantum readout would have to be maintained in motion. Since the paper reports no coherent operations, the appropriate description is mobile confinement, not mobile quantum computation. The result is an arXiv experimental preprint, and that publication status is part of its evidentiary weight. [1]

### Sources

1. [Alfaro et al. / arXiv — Demonstration of a mobile ion-trap quantum device, arXiv:2610.20487](https://arxiv.org/abs/2610.20487) — 2026-10-14.

## ESP32 / Signal Processing / Hackaday — Using ESP32-S3 Wi-Fi radio internals for raw I/Q transmission

Zephyr-based research code moves beyond receive samples into DAC playback. Peak sample clocks and actual usable RF bandwidth are different measurements.

Hackaday October 13, 2026; cyber-murmel/esp-sdr-zephyr documentation inspected. Hardware rates attributed to project authors, not independently reproduced.

The ESP32's Wi-Fi subsystem is usually exposed to applications as a packet engine. Beneath the familiar socket and Wi-Fi driver APIs, however, it uses mixers, converters, digital signal-processing blocks and sample buffers. The earlier ESPARGOS receiver work made raw in-phase and quadrature samples accessible to researchers. Hackaday's October 13 article reports a significant extension by cyber-murmel: a Zephyr module now describes raw waveform playback through an ESP32-S3 transmit DAC path as well as receive capture. This is access to a lower signal-processing layer, not an ordinary Espressif product feature or a certified general-purpose transmitter. [1]

Why I/Q? Each complex sample has one in-phase component and one quadrature component, representing orthogonal axes of a signal envelope. A sequence (1,0), (0,1), (−1,0), (0,−1) traces four successive quarter-turns of a phasor. That makes phase and amplitude modulation directly representable as numerical samples. The analog mixer and oscillator translate this low-frequency complex envelope toward RF. But the oscillator's tuning range, filters, gain calibration and amplifier behavior still constrain what comes out of the antenna. Access to sample memory does not create broadband analog hardware where none exists. [2]

The repository presents a Zephyr module with separate raw RX and TX interfaces, a sample ring, paced-sample operations, diagnostic capture and replay. Its example applications range from console surveys and a VITA 49.2 USB-streaming link to osmosdr-style tools compatible with GNU Radio or gqrx, plus experimental QAM/OFDM link implementations. The integration uses pinned Zephyr and Espressif HAL forks and specific RF-test dependencies. In other words, this is a stack-level modification involving radio registers, initialization, task scheduling and USB transport. Simply including one header in a stock Arduino sketch would not reproduce that environment. [3]

For the ESP32-S3 receive path, the documentation lists 256–16,380-sample bursts at nominal 80, 40 or 16 million samples per second; the TX playback engine lists 40 and 80 MS/s. Gapless playback has additional PSRAM and rate restrictions. Sampling rate must be distinguished from end-to-end streaming throughput. A 16,380-sample capture at 80 MS/s covers only 0.00020475 seconds, or about 205 microseconds. USB framing, host scheduler delays, buffer copies and the number of bytes per complex sample must all be budgeted if a process is to sustain continuous capture or playback. A peak engine clock is not a sustained application benchmark. [1] [2] [3]

Chip-specific behavior also matters. The project describes separate CPU-paced receive and transmit modes on the ESP32-C5 and C6 with rates up to about 250,000 samples per second, and an additional C5 modem diagnostic path. An advertised tuning API range of 100–6000 MHz does not mean an ESP32-S3 phase-locked loop locks across that interval. The developer states a narrower S3 PLL locking region of roughly 1.8–2.8 GHz. Likewise, waveform generation alone says nothing about spurs, harmonic suppression, receiver sensitivity or calibrated transmit power. All of those require analog measurements. [1] [2] [3]

**Analysis.** The most important caveat is explicit in the project's own README: it is unqualified for productive use, could permanently alter radio analog characteristics, and may produce noncompliant transmissions. Suitable conducted bench arrangements with shielding and attenuation are the appropriate research environment, not unlicensed arbitrary radiation. The transferable engineering idea is how much capability can exist below a peripheral's high-level protocol interface. Its layers—baseband samples, bus transport, calibrated analog chain and regulatory operating constraints—must be understood separately. The October 13 TX extension is new relative to earlier receiver-only ESP-SDR coverage, but the claimed rates have not been independently reproduced for this edition. [1] [2] [3]

### Sources

1. [Hackaday — ESP-SDR Can Now Transmit](https://hackaday.com/2026/10/13/esp-sdr-can-now-transmit/) — 2026-10-13.

2. [cyber-murmel / GitHub — esp-sdr-zephyr source and hardware notes](https://github.com/cyber-murmel/esp-sdr-zephyr) — Undated reference; checked 2026-10-17.

3. [ESPARGOS / GitHub — Upstream ESP-SDR raw receiver project](https://github.com/ESPARGOS/esp-sdr) — Undated reference; checked 2026-10-17.

## ESP32 / Community Sensor / ESPHome — Wi-Fi multipath as a local motion sensor: what CSI really measures

ESPectre packages channel-state changes as an automation event, with room-dependent calibration and fundamental limits for motionless occupants.

ESPectre project documentation checked October 17, 2026; r/Esphome discussion October 11. Original source code and public validation assets inspected; claims attributed to project.

A Wi-Fi receiver is continuously measuring a radio environment full of reflections. Walls, furniture and people create multiple signal paths with different delays and phases, and OFDM receivers estimate how those paths affect individual frequency bins. The resulting channel-state information, or CSI, can therefore behave as a crude environmental change sensor. Francesco Pace's ESPectre project uses this fact to report motion from ESP32 hardware, without adding a camera, microphone or dedicated radar IC. An October 11 post in r/Esphome discussed beta component integration; the original GitHub project additionally publishes SDK code, datasets, algorithms and setup documentation. That community venue is r/Esphome, not r/esp32. [1]

A simplified wireless observation model is Y_k(t)=H_k(t)*X_k(t)+noise. Here X is a transmitted known symbol on subcarrier k, H is the complex propagation response, and Y is the received quantity. As someone crosses a room, path lengths and reflecting surfaces change, disturbing the amplitudes and phases across some H_k values. A detector can compare time windows and turn the disturbances into a movement score. The challenge is that automatic gain changes, Wi-Fi packet timing, antenna placement and access-point behavior can produce variation unrelated to a person. The experimenter's task is separating meaningful changes from the radio's own nuisance variables. [2]

Motion is a different observable from occupancy. A stationary person may produce little channel variation, whereas a fan, opening door, pet or changed transmitter may produce plenty. The ESPectre README explicitly warns that it does not identify or count people and cannot prove that a room is empty. In particular, a low movement score does not demonstrate a lack of a breathing or sleeping person. Any security-sensitive use must treat the classification as uncertain and environmental. Unlike an imaging device, an RSSI or CSI feature vector does not directly supply a unique map of all objects contributing to the received signal. [3]

ESPectre lists classic ESP32, S2, S3, C3, C5 and C6 variants under supported paths, using normal 2.4-GHz Wi-Fi 4 infrastructure. That statement is specific to its implementation and does not mean those silicon revisions return identical CSI data formats or have the same peripheral limits. The project supplies native firmware, an embeddable C++ SDK, ESPHome and MQTT integrations, a Matter frontend and a MicroPython route. It also publishes a feature-selection ledger, recorded datasets and training procedure. Those artifacts allow verification of what was actually tested and which feature-engineering alternatives failed, rather than relying on a polished automation dashboard. [1] [2] [3]

The central scientific difficulty is domain shift. The channel itself depends on room geometry, wall materials, receiver position, multipath clutter, furniture and radio channel. A classifier trained and tested on temporally adjacent recordings from one room may appear accurate yet perform poorly elsewhere. Strong evidence would separate training and evaluation by space and session, report empty-room false alarms and missed motion across multiple installations, and include confidence intervals on comparable data. This edition did not independently benchmark the system and does not invent a cross-room detection percentage from repository promotional statements. [1] [2] [3]

**Analysis.** A useful implementation pattern is to keep RF acquisition bounded and cheap, move feature extraction to an independent task, and publish motion only after a hysteresis decision. For example, several windows above a higher trigger level could enter a 'moving' state, while several below a lower release level would clear it. That is an illustrative approach, not a verbatim claim about ESPectre's current classifier. Local inference may avoid cloud uploading raw CSI, but published motion events can still reveal home routines. The architecture is useful precisely because RF sensing, feature inference, automation output and access control are separable engineering concerns. [1] [2] [3]

### Sources

1. [francescopace / GitHub — ESPectre: source, SDK, CSI methods, datasets and evaluation](https://github.com/francescopace/espectre) — Undated reference; checked 2026-10-17.

2. [ESPHome — ESPectre integration reference](https://next.esphome.io/components/espectre/) — Undated reference; checked 2026-10-17.

3. [Reddit / r/Esphome — ESPectre beta ESPHome component discussion](https://www.reddit.com/r/Esphome/comments/1x3caty/espectre_is_now_a_beta_builtin_esphome_component/) — 2026-10-11.
