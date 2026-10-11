# Daily Digest — October 11, 2026 · Technical Edition

Nuclear clocks, spin-driven mechanics, photonic logic, and the hidden engineering inside ESP32 projects

Reporting cutoff: 2026-10-11T09:57:58-06:00 (America/Boise)

This replacement for the October 11 morning paper is a technical reading edition: six articles on what was measured, how the devices work, and calculations that make the results interpretable. Begin with nuclear-clock feedback and spin-driven motion, then explore photonic logic and three ESP32 system designs. Current studies and project reports are dated individually; older sources supply explicitly identified foundations. No politics or general-news roundup. Original explanatory calculations are labeled Analysis. The prior version remains in repository history.

## Physics · Precision measurement — A nucleus can now steer a clock. Here is what closes the loop.

Two October studies turn thorium spectroscopy into an operating frequency reference. The interesting advance is the feedback system—and the different meanings of stability, accuracy and a dark-matter limit.

Nature papers published October 7, 2026; Tsinghua laboratory account October 9. Vienna author manuscript posted June 3. Earlier work is identified as background, not a new discovery.

Two papers published in Nature on October 7 demonstrate a practical change in what a thorium-229 experiment does: a nuclear transition supplies feedback that controls a laser. The Vienna-led study is by Luca Toscani De Col and colleagues; the second, A nuclear clock synchronized to 229Th, is from Shiqian Ding’s Tsinghua-led collaboration. The result is not merely a sharper photograph of a spectral line. A measured frequency error is repeatedly converted into a correction, making the nuclear resonance an operating clock reference. [1] [2]

### From measuring a resonance to using it

The earlier 2024 JILA work connected the thorium transition to a strontium atomic clock through an ultraviolet frequency comb. That established a precise relationship between two very different oscillators. The new distinction is control: instead of using an existing clock to locate the nuclear resonance, the apparatus lets that resonance steer an oscillator. Measuring a tuning fork with a laboratory clock and building a clock regulated by that fork are different achievements. [3]

An ordinary optical atomic clock interrogates an electronic transition. Thorium-229 instead has an unusually low-energy nuclear excited state, around 8.4 electronvolts, accessible near 148 nanometres. That is still demanding vacuum-ultraviolet light, but it is far more accessible than the much higher energies associated with most nuclear transitions. The nucleus’s small size helps reduce some external perturbations; it does not make a thorium nucleus embedded in a crystal immune to its environment. [1] [2]

**Analysis.** A useful numerical check starts with frequency = speed of light / wavelength. Taking 148.4 nm gives approximately 2.02 × 10^15 cycles per second, and multiplying by Planck’s constant gives about 8.35 eV. These are rounded calculations, not new measurements. An optical counter cannot directly count every such cycle electronically. A frequency comb provides calibrated, evenly spaced optical reference lines; the beat between a laser and a nearby comb line falls into a measurable lower-frequency range. [2] [4]

### The discriminator is the essential component

**Analysis.** Picture an absorption dip with an unknown centre. Probe a little below the estimated centre and a little above it. If absorption is stronger on one side, the estimate is displaced. Their difference provides an error signal whose sign tells the controller which way to adjust the laser. Near the centre, write error ≈ slope × frequency offset. A steeper slope turns the same frequency mistake into a larger observable signal. Detector noise divided by that slope sets the uncertainty of an individual correction. [1]

Absorption readout avoids waiting for the nuclear state’s roughly ten-minute fluorescence lifetime. The Vienna apparatus uses a cavity-stabilized infrared laser and frequency multiplication to reach the nuclear transition, comparing the clock against a ytterbium-ion reference. Its experiments distinguish a 20-second feedback interval from a 30-minute interval. Short-term laser quietness and long-term correction are therefore separate engineering choices, not one precision number. [1] [5]

### Read the stability number as an instruction

Ding’s group reports a continuous-wave 148.4 nm source producing approximately 10 microwatts, with estimated sub-hertz linewidth, and absorption spectroscopy of thorium-doped calcium fluoride. Its reported fractional instability is 5 × 10^-13 / sqrt(tau/s), where tau is averaging time. Transition frequencies in independently prepared crystals agreed at the 10^-13 level. The account also describes making the crystal from only 1.4 micrograms of thorium-229. These are distinct demonstrations: laser performance, clock noise and cross-sample reproducibility. [2]

**Analysis.** Using that instability expression, averaging for 100 seconds gives 5 × 10^-14; 10,000 seconds gives 5 × 10^-15, provided the stated noise law remains applicable. Averaging one hundred times longer improves this particular noise contribution by ten, not one hundred. This square-root law is what independent random errors predict. A fixed offset, however, does not average away. Nor should the formula be extrapolated indefinitely through thermal drift, optical realignment or other changes in operating conditions. [2]

### Why a stable clock is not automatically an accurate one

The Vienna manuscript illustrates that distinction concretely: changing the illuminated region of a crystal produced line-centre differences up to 1.7 kHz, exceeding the reported 0.13 kHz statistical spread. Reusing a position was reproducible; local strain was proposed as an explanation. A quiet oscillator can therefore consistently reference a slightly different frequency after realignment. “Stable during a run” and “reproducible between runs” ask different physical questions. [5]

**Analysis.** For scale, 1.7 kHz divided by 2.02 × 10^15 Hz is approximately 8.4 × 10^-13. This is an illustrative conversion of a position-dependent shift, not an assigned total clock accuracy. It shows why quoting only the smallest statistical uncertainty would miss the practical problem. Reproducible beam placement and crystal uniformity can matter just as much as quieter electronics once random noise is sufficiently reduced. [5]

### A null result can still be a physics result

The Vienna team also searched for periodic changes in the nuclear-to-electronic frequency ratio and reported limits, not a dark-matter detection. The motivation is differential sensitivity: a hypothetical field might change nuclear and electronic transition energies by different fractions. Comparing two references then reveals a changing ratio even if neither reference can be regarded as absolutely unchanging. [1]

**Analysis.** In a simplified model, let each fractional shift equal K times a varying parameter: delta nu/nu = K delta alpha/alpha. The ratio responds to K_nuclear minus K_electronic. If both coefficients were identical, the effect would cancel; different coefficients make the comparison useful. Turning a limit on an oscillating ratio into a limit on a new field requires assumptions about those coefficients and the field model. The experiment supplies a bound on a measured quantity; the theoretical translation must remain visible beside it. [1]

### Sources

1. [Toscani De Col et al. · Nature — A thorium-229 optical nuclear clock with feedback loop](https://www.nature.com/articles/s41586-026-11084-4) — 2026-10-07.

2. [Tsinghua University · Department of Physics — Laboratory account of A nuclear clock synchronized to 229Th](https://www.phys.tsinghua.edu.cn/phyen/info/1154/2344.htm) — 2026-10-09.

3. [NIST / JILA — 2024 frequency-ratio measurement: the precursor, not the present advance](https://www.nist.gov/news-events/news/2024/09/major-leap-nuclear-clock-paves-way-ultraprecise-timekeeping) — 2024-09-04.

4. [NIST — Frequency combs: evenly spaced optical frequency references](https://www.nist.gov/noac/technology/quantum-optics-and-radiometry/frequency-combs) — Undated reference; checked 2026-10-11.

5. [Toscani De Col et al. · Author manuscript — Public technical manuscript, arXiv:2606.04997v1; earlier version of source 1](https://arxiv.org/html/2606.04997v1) — 2026-06-03.

## Physics · Spin–mechanical coupling — How a diamond’s spins move a 128-milligram resonator

Optical pumping changes a magnetic moment; a field gradient turns that change into force. A worked oscillator calculation makes the scale understandable without invoking a macroscopic quantum cat.

OIST announced the Science Advances study October 8, 2026, identifying October 7 publication. Detailed apparatus and numerical values below use the authors’ public May 18 manuscript, arXiv:2605.17750v1, rather than assuming every detail is unchanged in the final paper.

Anshuman Nayak, Daehee Kim, Shilu Tian and Jason Twamley report a connection between a quantum property inside diamond and visible-scale mechanics. Their apparatus optically changes the spin populations of nitrogen-vacancy defects. In a magnetic-field gradient, the resulting change in magnetic moment drives a levitated object’s motion. The new result concerns translational force on a comparatively massive resonator, not the discovery that spins and motion can interact at all. [1] [2]

### What light changes inside the diamond

An NV centre is a nitrogen substitution next to a missing carbon atom in diamond. The negatively charged centre has an electronic spin triplet. Optical excitation and spin-dependent relaxation let light redistribute the populations of its spin states. This makes it possible to prepare a different average magnetic response without physically attaching a current-carrying wire to the moving object. The relevant quantum system is the defect’s electronic structure; the word nuclear in the preceding clock article describes a different degree of freedom. [3]

**Analysis.** The magnetic energy of a small moment is U = -mu·B. Taking the spatial derivative gives a force, F_z = mu·dB/dz, when the moment is treated at the specified internal state. A uniform field can change spin energies and exert a torque, yet provides no translational gradient force in this approximation. A gradient supplies the missing position dependence. Optical preparation changes mu; it does not replace the magnetic field as the mechanism transmitting force to the object. [2]

### Separate support, actuation and measurement

The manuscript describes a diamond linked by a carbon-fibre rod to a slotted, diamagnetically levitated graphite plate. A mirror supplies interferometric displacement readout; a separate cylindrical magnet supplies the gradient near the diamond. The complete moving structure weighs 128 mg, resonates vertically at 17.6 Hz and has quality factor Q = 55 in air. Green 532 nm pumping produces motion of order 100 nm in air. The mass is the resonator assembly, not a 128 mg individual spin or necessarily the diamond alone. [2]

**Analysis.** This is a useful experimental architecture. One subsystem keeps the object suspended, another perturbs its internal state, a third converts that state change into a force, and a fourth measures motion. Those jobs need not share one physical interaction. Keeping them distinguishable makes it possible to alter the suspected drive while leaving the displacement measurement operational. It is the difference between seeing motion and constructing a causal account of why motion occurs. [1] [2]

### Convert the displacement into a force scale

**Analysis.** For a single mechanical mode, the driven equation is m x'' + (m omega_0/Q) x' + k x = F_0 cos(omega t), with k = m omega_0². Here m is moving mass, k is effective spring stiffness, omega_0 is angular resonance frequency and Q describes damping. Near resonance, the force adds energy in step with the motion, giving displacement amplitude approximately A = Q F_0/k. This is ordinary resonant amplification, even though the force-generating population changes originate in a quantum system. [2]

**Analysis.** Using m = 1.28 × 10^-4 kg and omega_0 = 2 pi × 17.6 s^-1 gives k ≈ 1.57 newtons per metre. A 100 nm resonant displacement would correspond to a sinusoidal force component of approximately 2.9 nanonewtons when Q = 55. This is our order-of-magnitude calculation, not the authors’ fitted force. Their chopped optical drive is not a pure sine wave; the calculation estimates the component at the mechanical resonance, not its instantaneous on–off peak. [2]

**Analysis.** The numbers also show the value of resonance. The same force applied statically would shift this effective spring only about 1.8 nm. At resonance, repeated pushes accumulate until damping balances the injected energy. Increasing Q could increase the amplitude without increasing the spin force, so displacement alone is not a fair comparison between differently damped experiments. A force measurement needs the mechanical susceptibility as well as a displacement calibration. [2]

### What the controls establish

The spin geometry is not simply “green light aligns every magnetic moment.” The manuscript treats four NV orientations and field-dependent state mixing. It reports controls removing the bias magnet and substituting 980 nm illumination that does not optically polarize the NV ensemble in the same way. A residual chopper-related peak is acknowledged. Those controls target alternative explanations such as a mechanical disturbance from the optical modulation apparatus. [2]

Earlier experiments drove NV spin transitions through mechanical strain. That is an important comparison, but not the same operation: strain-induced spin manipulation changes the internal spin system using vibration, while the new apparatus detects centre-of-mass motion driven by the spin-dependent force. “Spin–mechanical coupling” names a family of interactions. Identifying which coordinate is driven and which is measured prevents different experiments from being collapsed into a single claim. [4]

### Quantum source, classical motion measurement

**Analysis.** Finally, phase-locked driven motion is not evidence that the entire object occupies two spatially separated quantum states. For the stated mass and frequency, the harmonic ground-state displacement scale sqrt(hbar/(2m omega_0)) is about 6 × 10^-17 m. A 100 nm oscillation is roughly 1.6 billion times larger. That comparison does not disprove possible quantum protocols; it demonstrates why observing a driven oscillation alone cannot establish one. The achieved capability is a controlled internal-state-dependent mechanical actuator and a way to quantify its force. [1] [2]

### Sources

1. [Okinawa Institute of Science and Technology — First observation of quantum spins shifting a centimeter-scale object in the lab; publication information](https://www.oist.jp/news-center/news/2026/10/8/first-observation-quantum-spins-shifting-centimeter-scale-object-lab) — 2026-10-08.

2. [Nayak, Kim, Tian and Twamley · arXiv — Spin-force from a Nitrogen-Vacancy ensemble drives a 100 mg levitated resonator; public manuscript](https://arxiv.org/html/2605.17750v1) — 2026-05-18.

3. [Doherty et al. · Physics Reports / arXiv — The nitrogen-vacancy colour centre in diamond; foundational review, arXiv:1302.3288](https://arxiv.org/abs/1302.3288) — 2013-02-14.

4. [MacQuarrie et al. · Physical Review Letters / arXiv — Mechanical spin control of nitrogen-vacancy centers in diamond; earlier strain-coupling experiment](https://arxiv.org/abs/1306.6356) — 2013-06-26.

## Technology · Integrated photonics — A photonic logic chip built from resonances, not miniature transistors

A September experiment combines nonlinear films, microrings, an integrated light source and computationally designed interconnects. Its component response time is not yet a processor clock rate.

Light: Advanced Manufacturing 7, article 107, published September 18, 2026. This is a recent-study explainer, not an October 11 announcement. The inverse-design references are explicitly older foundations.

Yumeng Chen and colleagues report a hybrid photonic circuit with a whispering-gallery micro-laser, four bismuth-telluride/silicon microrings and inverse-designed optical interconnects. Their September 18 paper demonstrates selectable two-bit optical outputs. Silicon waveguides are 500 nm wide and 220 nm thick, with 50 nm Bi2Te3 films on the relevant structures. The reported 1.5 micrometre spacing is between components; it is not a claim that an entire packaged computer occupies that dimension. [1]

### Translate the device into phase accumulation

**Analysis.** A ring is useful because light returning after one circuit can reinforce the field already inside it. In a simplified uniform ring, resonance requires m lambda = n_eff L: m is an integer, lambda the vacuum wavelength, n_eff the effective refractive index and L the circumference. At a resonance, coupling between the straight waveguide and ring changes the outgoing light strongly. Away from resonance the same geometry can transmit very differently. Frequency therefore becomes a controllable routing variable. [1] [4]

**Analysis.** Suppose the optical path length increases slightly while the physical ring is unchanged. The wavelength satisfying that phase condition also increases. To first order, ignoring dispersion, delta lambda/lambda ≈ delta n_eff/n_eff. Nonlinear optical materials supply one way to change the effective index: in a simple Kerr description, n = n_0 + n_2 I, where I is optical intensity. Higher intensity modifies the propagation itself. This is a mechanism for making one optical signal influence another rather than merely carrying data down an unchanged fibre. [1] [2]

The experiment combines differently patterned coated resonators, including anti-parity–time-symmetric structures, with compact splitters and crossings. It reports approximately 1 nm pump-induced redshift and pump–probe transients lasting hundreds of femtoseconds. Packaged measurements use an electrically driven, butt-coupled III–V micro-laser and distinguish outputs 00, 11, 10 and 01. The authors identify coupling efficiency, long-term stability, film oxidation and delamination as issues for further work. [1]

### A small shift can matter more than a large device

**Analysis.** For intuition, a 1 nm shift near 1550 nm is a fractional wavelength change of about 6.5 × 10^-4. With the simplified relation above and an assumed effective index of 2.4, the equivalent index change would be roughly 0.0015. That is an illustration, not a recovered material constant for this hybrid ring: dispersion, field overlap and coupled modes modify the conversion. It shows why a small change in optical path can move a narrow resonance enough to alter an output substantially. [1]

Inverse design tackles another obstacle: fitting the paths between the active elements into little space without excessive leakage or reflection. A designer specifies a desired electromagnetic outcome, such as delivery to one output with suppression at another. An optimizer changes a distribution of material. The adjoint method makes this practical by obtaining gradients for many design variables from a small number of field solves, rather than perturbing each geometric parameter and rerunning a full simulation separately. [2]

**Analysis.** Consider an illustrative design grid with 10,000 independently adjustable cells. Straightforward finite differences need approximately one extra field solution per cell for a gradient. An adjoint construction can obtain the corresponding sensitivity information with a forward and an adjoint solve under its model assumptions. It does not make the optimization trivial: each solve still costs computation, an initial design can reach a poor local optimum, and manufacturable widths and material loss constrain what the optimizer may choose. [2]

### Do not convert femtoseconds into a computer benchmark

There is a useful caution in the older methods literature itself. A 2021 correction to the nonlinear-adjoint paper clarifies that the simple electric-intensity expression used in its demonstration applies to a particular two-dimensional polarization model. A formula that is valid in a scalar simulation is not automatically a full vector treatment of every material. That does not invalidate inverse design; it explains why the physical model must be checked before an attractive optimized shape is trusted. [3]

**Analysis.** A pump–probe transient measures how a selected response changes after excitation. A usable logic system must additionally deliver light, settle its resonators, maintain distinguishable outputs, drive subsequent stages and read results. If stored optical energy decays with lifetime t, a resonance’s quality factor scales as Q ≈ omega t. Sharper spectral selection can therefore coexist with a longer energy-storage time. The shortest local response is not necessarily the slowest step in a complete signal path. [1] [4]

**Analysis.** The technical achievement is a working combination of source integration, nonlinear resonators and very compact routing. It is not yet evidence of a general-purpose processor running at the inverse of a femtosecond material response. The productive engineering question is which operations benefit from remaining optical, and whether the savings survive coupling loss, detection and signal regeneration. This experiment supplies a concrete circuit to investigate those questions, rather than a replacement specification for an electronic CPU. [1]

### Sources

1. [Chen et al. · Light: Advanced Manufacturing — Ultra-compact integrated photonic logic chip; DOI 10.37188/lam.2026.107, open access CC BY 4.0](https://www.light-am.com/en/article/doi/10.37188/lam.2026.107) — 2026-09-18.

2. [Hughes, Minkov, Williamson and Fan · ACS Photonics — Adjoint Method and Inverse Design for Nonlinear Nanophotonic Devices](https://pubs.acs.org/doi/10.1021/acsphotonics.8b01522) — 2018-12-07.

3. [Hughes et al. · ACS Photonics — Correction: limits of the scalar intensity-dependent model](https://pubs.acs.org/doi/10.1021/acsphotonics.1c00396) — 2021-04-22.

4. [NIST — Miniature microring frequency-comb explanation; optical resonance background](https://www.nist.gov/news-events/news/2022/02/scientists-greatly-expand-frequencies-generated-miniature-optical-ruler) — Undated reference; checked 2026-10-11.

## ESP32 · Radio and high-rate data paths — The ESP32-S3 can expose raw radio samples. Getting them out is the hard part.

A project discovered through r/esp32 and Hackaday makes the distinction between an RF sample rate, a memory transfer rate and a sustained external stream unusually clear.

Hackaday coverage October 3, 2026. Creator’s r/esp32 post and current eSpDR/ESPARGOS project documentation checked October 11. Reddit’s cached relative timestamp was not reliable enough to assign an original posting date.

The interesting discovery is inside the radio, not the familiar general-purpose ADC pins. The eSpDR creator’s r/esp32 post reports access to raw in-phase and quadrature samples from the ESP32-S3 receive chain, before normal Wi-Fi packet processing. Hackaday subsequently covered both this work and an independent ESPARGOS route. Bypassing packet interpretation lets software inspect a waveform that the normal Wi-Fi API would never expose as arbitrary received samples. [1] [2]

### What the sample format buys you

**Analysis.** An I/Q pair represents one complex sample, z = I + jQ. Mixing against two oscillator phases retains information that a single envelope measurement loses: the direction in which phase rotates distinguishes frequencies above and below the tuned centre. Computing magnitude sqrt(I² + Q²) deliberately throws that phase information away. It is useful for burst detection, but it is not equivalent to preserving the waveform for later demodulation or phase-sensitive analysis. [4]

ESPARGOS documents signed ten-bit I and Q values within wider capture words, with additional gain-related information. The receive path can write samples into internal memory at a rate far above a serial link’s delivery rate. A burst captured quickly and uploaded slowly can produce a spectrum, but it does not observe everything between bursts. For a receiver studying short intermittent events, that difference is a measurement limitation, not just an inconvenient user interface. [4] [5]

### Do the bandwidth arithmetic before choosing a cable

**Analysis.** At 80 million complex samples per second, twenty useful sample bits per pair amount to 1.6 gigabits per second, or 200 megabytes per second. Store each pair in a 32-bit word and the memory traffic becomes 320 MB/s. Those two rates describe the same signal. Packing removes representation overhead; it does not reduce the information in the twenty sample bits. Conversely, “80 MHz sample rate” does not promise a flat 80 MHz analogue passband. [3] [4]

The current eSpDR design uses both 240 MHz S3 cores to drive two eight-bit GPIO lanes into an Artix-7 FPGA. The published packing kernel emits forty bytes in ninety-one cycles per lane, approximately 211 MB/s across both lanes before other overhead. FPGA logic orders the data, compresses it losslessly and buffers it in 256 MiB of DDR3 before an FT600 USB interface. The author reports typical compressed input around 95–100 MB/s against about 190 MB/s sustained USB delivery. [3]

**Analysis.** That architecture makes a seemingly strange design choice understandable: an FPGA and external memory can be necessary even when the radio samples already exist inside a cheap microcontroller. The bottleneck has moved from digitization to extraction. At this point “add a faster serial port” is not enough; packing instructions, SRAM access and the receiving circuit’s sampling edge all form one timed transport. This is an external hardware project, not an ELF app that a normal ESP32-S3 board can simply run in the background. [1] [3]

### Why clock and memory placement become protocol details

The current README describes a forwarded 20 MHz I2S master clock on GPIO41, with the ESP keeping its own crystal. The FPGA derives its sampling clock from that forwarded reference. Separate SRAM placement for the two transmit kernels avoids stalls. This is newer wiring than the original creator post’s external-reference arrangement; the two descriptions should not be combined into one build recipe. [3]

**Analysis.** Suppose independent transmitter and receiver oscillators differ by only ten parts per million. After one millisecond their timing differs by ten nanoseconds. A byte held for two cycles of a 240 MHz processor lasts about 8.3 nanoseconds. The clocks can therefore move through an entire byte window in roughly a millisecond. Forwarding a common reference addresses that accumulated drift. It still leaves fixed propagation delay and edge placement to calibrate. Likewise, a surprise instruction-fetch stall is effectively a protocol timing error. [3]

### The FIFO cannot repeal an average-rate mismatch

**Analysis.** Buffering solves a different problem. The documented uncompressed fallback stream, including record headers, is 202.5 MB/s. If it stayed incompressible while USB drained 190 MB/s, an initially empty 256 MiB buffer would fill in about 21 seconds: capacity divided by the 12.5 MB/s deficit. This idealized calculation ignores other overhead. More memory postpones overflow; it cannot make a permanently slower consumer keep up. Successful sustained operation depends on the actual compression distribution and host behaviour. [3]

**Analysis.** For analysis, an N-point complex FFT has frequency-bin spacing sample_rate/N. With N = 4096 and 80 MS/s, that is about 19.5 kHz; a block spans 51.2 microseconds. A longer FFT improves bin spacing while averaging over a longer event interval. Decimation can reduce processing and transport load, but only after filtering the unwanted bandwidth so it does not alias into the retained band. These are choices about what information the instrument keeps, not free speed improvements. [4]

The reusable result is a way of thinking about the complete signal path: RF bandwidth, sample representation, producer timing, transport capacity, buffering and analysis resolution must agree. The repository’s physical-run reports remain the developer’s measurements, not an independent qualification here. The firmware also relies on chip-specific receive internals, so a working S3 path is not a promise that the same registers, performance or analogue characteristics apply to every ESP32 variant. [3] [5]

### Sources

1. [h0m3us3r · Reddit r/esp32 — Creator report: raw IQ streaming from ESP32-S3 at 80 MS/s](https://www.reddit.com/r/esp32/comments/1wq37xz/got_raw_iq_streaming_out_of_an_esp32s3_at_80_mss/) — Undated reference; checked 2026-10-11.

2. [Jenny List · Hackaday — The ESP32, An SDR In Itself](https://hackaday.com/2026/10/03/the-esp32-an-sdr-in-itself/) — 2026-10-03.

3. [h0m3us3r · eSpDR — Current architecture, throughput budget, memory placement and measurements](https://github.com/h0m3us3r/eSpDR) — Undated reference; checked 2026-10-11.

4. [ESPARGOS project — ESP32 software-defined-radio capture: raw sample layout and board-dependent limits](https://espargos.net/espsdr/) — Undated reference; checked 2026-10-11.

5. [ESPARGOS project · GitHub — esp-sdr receiver firmware and supported targets](https://github.com/ESPARGOS/esp-sdr) — Undated reference; checked 2026-10-11.

## ESP32 · Optical communication — One LED can transmit, receive and help pair two devices

PacketLED turns a junction-capacitance trick into a packet link. SecurePair adds a separate authentication protocol, making this a useful study in keeping physical communication and trust distinct.

Hackaday article October 5, 2026; PacketLED PHY source identifies v1.1.0 dated October 1. Current project and protocol documentation checked October 11. The underlying LED-sensing technique dates back at least to the cited 2003 research.

Luca Soltoggio’s project uses one ordinary LED at each end as both emitter and light sensor. Hackaday’s October 5 article led to two distinct libraries: PacketLED handles optical communication; SecurePair handles pairing and encrypted messages. The author explicitly describes the latter as a beta without a cryptographer’s review. That separation is important: a clever physical link is not automatically a secure one. [1]

### Read the actual receiving routine

The physical idea is older than this implementation. Dietz, Yerazunis and Leigh described bidirectional LED sensing and communication in 2003. A semiconductor junction that emits light when driven can also respond to incident light. Its capacitance and light-generated current provide a signal even without a separate photodiode or analogue amplifier. What the current project adds is a usable link implementation around that effect, not a new law of semiconductor optics. [4]

PacketLED’s Arduino PHY first drives the cathode high and anode low, reverse-biasing the LED. After a 20-microsecond setup delay, it changes the anode to an input, waits a specified integration window and samples that pin with the ADC. The cathode remains driven during integration. It then returns both pins low. Transmission reverses the job: the anode is driven high and cathode low, so the LED emits. Firmware is switching the same junction between two roles. [3]

**Analysis.** An approximate model is delta V = I_photo × delta t / C, where I_photo is photocurrent, delta t the integration window and C the effective capacitance at the sensing node. Doubling the collection time ideally doubles the voltage change, but also halves how often an independent reading can be completed. Stray capacitance from wiring increases C and lowers the voltage change. Thus short wires are not merely tidier: they can alter the sensor’s sensitivity and timing. [3] [4]

The implementation selects 12-bit ADC resolution and zero-decibel attenuation to work with a small voltage range. Its source warns that setting the default attenuation also affects other analogue inputs in the sketch. That is a concrete integration consequence: a reusable optical-link library can silently change the assumptions of an unrelated analogue sensor unless the application restores or explicitly manages each channel’s configuration. [3]

### A packet link is more than blinking bits

The PacketLED README reports 256, 512 and 1024 bit/s modes, up to 64 payload bytes, CRC-16, acknowledgements, retransmission and duplicate suppression. Clear narrow-beam LEDs reportedly reached about 2.5 metres; diffused LEDs produced much shorter range. The claims depend on the components and arrangement. A pin must support both output and the required ADC role; an input-only pin is not interchangeable just because it can measure voltage. [2]

**Analysis.** At 1024 bit/s, sixty-four payload bytes alone require 512/1024 = half a second. Headers, framing, acknowledgement and turn-around add time, and a retry adds more. This link is consequently plausible for pairing material or small commands, not a substitute for a high-rate radio data feed. Duplicate suppression matters even at low speed: if an acknowledgement is lost, retransmitting an already received command must not necessarily repeat its physical side effect. [2]

### Why light does not remove the authentication problem

SecurePair can use light for the initial exchange and ESP-NOW for subsequent traffic. Its documented construction combines X25519 key agreement, HKDF-SHA256 key derivation and AES-256-GCM authenticated encryption, with a twenty-bit short authentication string presented for user comparison. Physical tests are reported for ESP32-C3/C6 and ESP-NOW; the README distinguishes LoRa support from completed physical validation. This is a reported implementation, not an independently audited security certification. [5]

Key agreement alone establishes a secret with whoever completed the exchange; it does not prove that this is the device the user intended. SecurePair’s protocol commits to values before revealing them and binds the exchange transcript into key derivation and the displayed comparison. The purpose is to prevent a participant from freely adapting a final value after seeing everything from the other side. Explicit confirmation then decides whether the derived peer relationship should be accepted. [6]

**Analysis.** A uniformly distributed twenty-bit comparison has 1,048,576 possibilities. Under the intended protocol assumptions and correct user checking, an attacker trying to match one independent trial has a probability on the order of one in a million. That calculation is not a complete security proof: repeated trials, implementation errors, poor randomness or a user accepting a mismatch change the situation. Nor does an unobstructed LED path establish that no other observer can receive the light. [5] [6]

The repository also makes the nonce problem visible. AES-GCM requires avoiding nonce reuse under one key; its documented scheme combines a persistent boot counter with a message counter. Persistence is therefore part of the cryptographic design, not just a convenience setting. This project’s most transferable lesson is the layered architecture: understand the junction as a sensor, make transmission into a reliable packet service, and treat authentication and crash-safe cryptographic state as separate problems. [5] [6]

### Sources

1. [Jenny List and project author Luca Soltoggio · Hackaday — Two Microcontrollers Talking, All It Needs Is An LED](https://hackaday.com/2026/10/05/two-microcontrollers-talking-all-it-needs-is-an-led/) — 2026-10-05.

2. [Luca Soltoggio · PacketLED — Library architecture, wiring, rates and reported range](https://github.com/toggio/PacketLED) — Undated reference; checked 2026-10-11.

3. [Luca Soltoggio · PacketLED source — LedPhyArduino.cpp: reverse bias, integration window and ADC readout](https://github.com/toggio/PacketLED/blob/main/src/LedPhyArduino.cpp) — 2026-10-01.

4. [Dietz, Yerazunis and Leigh · Mitsubishi Electric Research Laboratories — Very Low-Cost Sensing and Communication Using Bidirectional LEDs, TR2003-35](https://www.merl.com/publications/TR2003-35) — Undated reference; checked 2026-10-11.

5. [Luca Soltoggio · SecurePair — Pairing, transport, tests and security limitations](https://github.com/toggio/SecurePair) — Undated reference; checked 2026-10-11.

6. [Luca Soltoggio · SecurePair protocol — Protocol transcript, commitments and confirmation flow](https://github.com/toggio/SecurePair/blob/main/docs/PROTOCOL.md) — Undated reference; checked 2026-10-11.

## ESP32 · Systems architecture — An ESP32 can be a Linux radio, not just a networked application

An October build guide and Espressif’s current hosted stack show how to separate the application processor from Wi-Fi. Credit counters and measured throughput explain more than the bus label.

Arya Voronova’s firsthand Hackaday build article published October 7, 2026. Official ESP-Hosted-Linux architecture and performance documentation checked October 11; performance rows are reference measurements, not new measurements made for this edition.

Arya Voronova’s October 7 build article treats an ESP32 as a peripheral for a Linux computer: flash matching radio firmware, attach it over a supported bus and load the corresponding Linux driver. The useful change in perspective is that the ESP need not own the end-user application. A Linux system can retain its normal applications and networking tools while an inexpensive microcontroller supplies the radio functions. [1]

### Choose the software boundary before the board

Espressif’s ESP-Hosted-Linux exposes Wi-Fi through cfg80211/nl80211 and a normal wlan network device, with standard tools such as wpa_supplicant and hostapd. Bluetooth uses Linux HCI integration. Its current transport table supports SDIO on ESP32, C5, C6 and C61; S3 is listed for SPI, not SDIO. Available radio modes still depend on the chip. A software layer cannot manufacture a radio or bus peripheral missing from the selected silicon. [2]

A network co-processor and an application talking through AT commands are not the same interface. With a native Linux network device, ordinary applications can use the operating system’s networking abstractions; they do not each need a bespoke serial-command parser. ESP-Hosted-MCU addresses a related but different host environment, using a hosted interface and remote procedure calls for MCU applications. Choosing between the stacks is an architectural decision about which side owns which services, not merely selecting a faster connector. [2] [5]

### Flow control is the part the wiring diagram omits

Follow one transmit packet in the SDIO implementation. Linux has a frame to send; the ESP has a finite number of receive buffers. The host reads buffer-credit information and sends a CMD53 transfer only when enough space is available. The documented counters are cumulative values with wrap masks. On receive, the ESP advances an accumulated byte count and interrupts the host; Linux computes how much unread data exists and retrieves it. A notification and the data accounting are different things. [3]

**Analysis.** Why use a cumulative count instead of treating every interrupt as one packet? Imagine that three packets arrive before the host services the first interrupt. A count or accumulated length still describes all unread work, even if notifications coalesce. Conversely, an interrupt can wake a consumer that then finds a state already serviced elsewhere. The transport must derive work from shared state, not assume a one-to-one relationship between electrical events and application messages. [3]

**Analysis.** Counter wrapping is manageable when subtraction follows the protocol’s modulus and the producer cannot lap the consumer ambiguously. With an illustrative eight-bit counter, a previous value of 250 and a new value of 4 represent an advance of ten, not a negative change of 246. Buffer credits limit how far the producer may proceed. This is the same general principle behind a bounded ring buffer: indices describe progress, while the capacity contract prevents unread data from being overwritten. [3]

### A bus ceiling is not a Wi-Fi benchmark

**Analysis.** For an electrical ceiling, four data lines clocked at 41.67 MHz carry at most about 166.7 megabits per second in the active transfer direction before protocol overhead. This does not establish full-duplex application throughput. Command handling, turn-around, headers, copying, scheduling and the wireless link consume time. The useful number is not the bus clock alone but the rate at which the entire producer–consumer chain completes real traffic. [3] [4]

The official reference table reports C6 SDIO values including TCP 41.7/51.0 Mbps and UDP 90.4/58.4 Mbps for its 40 MHz radio-width row. At 20 MHz radio width the TCP entries are 40.9/55.6 Mbps. Those rows used a Raspberry Pi 4B and a 41.67 MHz SDIO clock. The documentation cautions that some endpoint-direction methodology is incomplete; the labels are preserved rather than promoted into a fully reproducible benchmark specification. [4]

**Analysis.** The apparently better TCP entry at narrower radio width is a good warning against “twice the bandwidth means twice the application rate.” The radio is one constraint among several, and the result also depends on direction and test conditions. These rows do not isolate a causal explanation for the difference. They do establish that physical bus capacity and useful TCP throughput are different quantities, and that widening one part of the path does not guarantee an improvement at its end. [4]

The architecture provides a practical debugging sequence: establish power and signal integrity, confirm device enumeration, verify interrupt and counter behaviour, then test raw transport before blaming the wireless stack. Espressif includes a raw-throughput mode that bypasses normal Wi-Fi traffic specifically for this separation. A bus-only test cannot establish radio performance, but it can show whether a higher layer is being asked to solve a problem already present beneath it. [3] [4]

**Analysis.** For a new instrument, this suggests a disciplined partition. Put the large interface, files and analysis on the host; put timing-sensitive radio service on the co-processor; make the boundary observable with queue lengths, credits and error counters. Keep host-driver and co-processor-firmware versions compatible, and treat each ESP32 variant’s documented interfaces explicitly. The interesting capability is not simply adding Wi-Fi. It is making the processor boundary a testable part of the system rather than an opaque source of stalls. [1] [2] [5]

### Sources

1. [Arya Voronova · Hackaday — ESP32 As Your Raspberry Pi’s Linux Wireless Co-processor](https://hackaday.com/2026/10/07/esp32-as-your-raspberry-pis-linux-wireless-co-processor/) — 2026-10-07.

2. [Espressif · ESP-Hosted-Linux — Linux networking interfaces, supported targets and architecture](https://github.com/espressif/esp-hosted-linux) — Undated reference; checked 2026-10-11.

3. [Espressif · ESP-Hosted-Linux — SDIO transport: buffers, counters, CMD53 transfers and recovery](https://github.com/espressif/esp-hosted-linux/blob/master/docs/architecture/sdio.md) — Undated reference; checked 2026-10-11.

4. [Espressif · ESP-Hosted-Linux — Performance and raw transport: per-target measurements and test qualifications](https://github.com/espressif/esp-hosted-linux/blob/master/docs/reference/performance.md) — Undated reference; checked 2026-10-11.

5. [Espressif · ESP-Hosted-MCU — MCU-hosted Wi-Fi architecture and RPC interface](https://github.com/espressif/esp-hosted-mcu) — Undated reference; checked 2026-10-11.
