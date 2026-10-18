# Daily Digest — October 18, 2026 · Technical Discovery

Kagome flat bands, molecular attosecond delays, Floquet photonics, niobium carbide growth and ESP32 builds

Reporting cutoff: 2026-10-18T08:49:19.273Z (America/Boise)

This Sunday's paper examines four studies published on October 15 and three ESP32 builds reported October 14–15, including updated source for an iPhone automation project as of October 18. It emphasizes the apparatus, mathematics, engineering choices and observed results. Numeric quantities are only as strong as the accessible papers or project records: inaccessible methods tables, developer-only measurements and proposed features are specifically distinguished from established findings. Articles are fully readable offline.

## Physics · Quantum materials · Research feature — A natural monolayer kagome lattice brings a flat band within reach of gating

Interference on corner-sharing triangles suppresses electron dispersion; the new platform holds over 220 times the flat-band electron density of moiré counterparts.

Nature Physics published 15 October 2026; the full article is subscription-limited. Abstract and source-data description consulted; detailed numerical uncertainty and phase diagrams unavailable.

An electronic flat band is a regime in which electron energy changes little as crystal momentum changes. In a kagome lattice, corner-sharing triangles produce loops with multiple paths between sites. Quantum wave amplitudes pick up phases along each path. When the alternative paths interfere destructively, certain states cannot propagate with the usual dispersive energy-momentum relation. The limiting tight-binding model contains a band that is independent of momentum. In a material, distortions, longer-range hopping and interactions generally make that ideal picture approximate. The important property is a narrow kinetic-energy scale, not motionless electrons. [1]

The group velocity of a Bloch wave packet is v = (1/hbar) dE/dk: E is band energy, k crystal momentum and hbar the reduced Planck constant. The flatter E(k) becomes, the smaller this velocity scale in the ideal single-particle picture. The ratio U/W, an interaction energy U over bandwidth W, can become large. Correlations, magnetic order and other collective responses are then energetically competitive, but so is disorder if its broadening is comparable with W. The presence of a flat band does not prove superconductivity or a particular many-body phase. [1]

Hyungkun Bong, Choongjae Won, Seongyong Lee and collaborators report a natural van der Waals family A2T3X4, with A an alkali metal, T a transition metal and X a chalcogen. Previous flat-band experiments have often used three-dimensional kagome crystals or artificially formed moiré superlattices of twisted layers. Here the kagome geometry belongs to an intrinsically two-dimensional sheet. The reported characterization reaches the monolayer limit. Figure descriptions identify A2Pd3S4 as a measured member of the family. [1]

The electronic evidence comes from nanofocused angle-resolved photoemission spectroscopy, nano-ARPES. Photons remove electrons; emitted energies and angles map the occupied electronic spectral function versus in-plane momentum. A small focused beam helps isolate microscopic exfoliated regions instead of averaging a thin flake with thicker surroundings. A nearly horizontal feature in momentum-energy space, reproduced across suitable samples and measurements, is a more direct probe of band flatness than simply finding a resistivity anomaly. Photoemission nonetheless does not determine the full spectrum above the chemical potential. [1]

The paper reports an isolated kagome-derived band just below the Fermi level. Electrostatic gating moves this band to the Fermi level, where partial filling can become possible. That adjustment matters: a perfectly narrow but fully occupied band is not the same correlated electronic problem as a partially occupied one. Gating alters carrier density without preparing another compound for every desired filling; it provides an independent experimental axis for comparing spectral and transport responses. [1]

The authors state that their platform's flat-band electron density exceeds those of existing moiré-based artificial flat-band systems by more than 220 times. The intuitive scale is unit-cell area: a crystal lattice has a much smaller real-space period than a moiré pattern, so the number of band states available per unit area can be far larger. This is a measured or calculated electronic-density comparison described by the authors, not a demonstrated 220-fold improvement in critical temperature, power efficiency or conductivity. [1]

That distinction is the central limitation. The accessible paper abstract describes a platform for potentially higher-temperature flat-band phenomena, not an already demonstrated high-temperature ordered phase. It supplies no verified full-bandwidth value, disorder broadening, gating calibration or transition curve for us to reproduce here. The accompanying source-data deposit is a useful audit route. Subsequent work must establish whether U/W is large in experimentally clean samples and whether a thermodynamic or transport signature tracks the tunable filling. [1] [2]

Broadly, the discovery shifts the design space from extremely large engineered moiré cells toward the much denser microscopic kagome geometry of a naturally thin crystal. What changes is the available band structure and how it can be tuned; which interaction-driven state emerges remains an open measurement, not a conclusion to be imported from theoretical flat-band proposals. [1]

### Sources

1. [Bong et al., Nature Physics — Monolayer van der Waals kagome lattice for high-temperature flat-band physics](https://www.nature.com/articles/s41567-026-03492-0) — 2026-10-15.

2. [Bong et al., Zenodo — Monolayer kagome source data](https://doi.org/10.5281/zenodo.22076867) — Undated reference; checked 2026-10-18.

## Physics · Ultrafast molecular dynamics — A photoelectron's delay depends on the electronic state of the NO+ ion

Attosecond interferometry separates changes in electronic scattering from changes in the ion's vibration.

Peer-reviewed Communications Physics study published 15 October 2026. The accessible abstract does not expose numerical channel-by-channel delay and uncertainty tables.

An electron released by a photon is not a classical projectile whose departure instant can be identified with a detector's click. The optical transition has a complex quantum amplitude, and the phase of that amplitude changes with the outgoing electron's energy. Ultrafast interferometry can compare amplitudes from alternative pathways and recover relative phase information. The observable 'photoemission delay' is usually a wave-packet group-delay quantity associated with that phase evolution, not a literal transit time recorded by a miniature clock. [1]

A useful relation is tau(E) = hbar dphi(E)/dE. Here phi is the scattering or transition phase, E the electron kinetic energy and hbar Planck's reduced constant. A rapidly varying phase near a resonance creates a steeper derivative and an enhanced inferred delay. An attosecond is 10^-18 second; resolving effects on that scale demands coherent optical interference and precise electron energy selection rather than electronics that switch in an attosecond. [1]

Huiyong Wang, Guangru Bai and collaborators examined nitric oxide, NO, a heteronuclear diatomic molecule. After removing an electron, its molecular ion NO+ can occupy different electronic states, and each electronic state admits a ladder of vibrational levels. Photoelectron energy depends on which ionic state remains. High energy resolution helps separate those final-state channels before their phases are compared. Without this distinction, averaging several channels would conceal precisely the electronic and nuclear dependencies the experiment seeks. [1]

The published study combines attosecond interferometry with scattering calculations. It reports significant differential delays between photoionization channels that leave the molecular ion in different electronic states. Between different vibrational levels of the ionic electronic ground state, in an interval without strong resonances, it reports negligible differential delays. That contrast is not a claim that vibrational motion cannot affect electrons. It means the probed non-resonant vibrational channels share sufficiently similar phase slopes that the experiment does not resolve the same kind of timing difference. [1]

Scattering resonances supply a physical explanation. An outgoing electron can couple transiently to a quasi-bound molecular configuration and emerge with a sharply energy-dependent phase. A different electronic state changes the molecular ionic potential and available scattering structure, potentially producing different resonances or phase responses. Merely changing the vibrational quantum number within the same electronic surface can shift thresholds without similarly changing the phase slope in a non-resonant energy window. [1]

The group also compares theory with measurements averaged over molecular orientations. A fixed-orientation molecule can produce angle-dependent photoemission phases, so orientation averaging removes some information. The reported agreement despite this averaging supports their scattering description at the observed level, but cannot establish a complete molecular-frame electron trajectory. A stronger test could prepare aligned molecules and map energy and orientation jointly. [1]

Numerical integrity matters here. The accessible abstract describes qualitative delay differences and agreement with theory, but does not supply the full list of measured delays, uncertainties or resonance energies. Quoting a plausible-sounding number of attoseconds from a different molecule would misrepresent this paper. The established conclusion is channel selectivity: differential delay is substantial across electronic final states, but weak across selected vibrational states away from resonances. Phase-sensitive spectroscopy therefore adds a dimension of testing beyond photoelectron intensity alone. [1]

### Sources

1. [Wang, Bai et al., Communications Physics — Capturing attosecond delays in electronic and vibrational dependent photoemission of NO molecules](https://www.nature.com/articles/s42005-026-02911-1) — 2026-10-15.

## Physics · Photonic lattices — A twist of optical polarization changes a coupling constant's sign

Periodically twisted guides control positive and negative interaction amplitudes and reverse the direction of topological edge-state circulation.

Peer-reviewed Nature Communications article published 15 October 2026. Abstract and metadata accessible; device-specific numerical losses, widths and tolerances not independently read.

Neighboring optical waveguides exchange energy because their evanescent electromagnetic fields overlap. In a standard coupled-mode approximation, i da_m/dz = sum_n J_mn(z) a_n, with propagation distance z, complex field amplitude a_m in guide m and coupling coefficient J_mn between guides. Two fixed guides exchange power periodically. More sophisticated synthetic-lattice designs, however, need to tune not only the magnitude of J but also its sign while propagation continues. [1]

A negative coupling is a statement about relative wave phase, not an optical intensity less than zero. For one isolated pair of sites a sign may be removed by redefining a mode's phase. In a network with closed loops, or with couplings varied in a particular sequence, relative signs affect interference and can act like an artificial gauge field. The order and geometry of those signed interactions matter as much as which sites are connected. [1]

Jinze Gao, Guibin Li, Zhuochen Du and collaborators created twisted photonic waveguide arrays. As the guides twist, the relative polarization angle of adjacent waveguide modes changes. That changes their effective coupling, allowing it to move continuously from positive, through zero, to negative, with controllable magnitude. The authors contrast this with earlier Floquet waveguides relying mainly on geometric path modulation, separate auxiliary structures or limited phase engineering. [1]

Floquet theory characterizes dynamics when the governing coefficients repeat periodically. In paraxial photonics propagation distance plays the mathematical role of time: the structure repeats after a length Lambda, and the one-cycle propagation operator U(Lambda) describes an effective driven system. Its eigenphases create bands analogous to quasienergy bands. The response generally cannot be predicted merely by replacing the oscillating coupling with its numerical average, because phases accumulate in order during propagation. [1]

The paper investigates one-dimensional arrays with Floquet flat bands and optical oscillations that return after n times the geometric period Lambda. A field pattern may therefore require several physical twists to complete its full recurrence, even though the material geometry repeats each Lambda. In two-dimensional lattices, the researchers also report reversal of the chirality of topological edge states. Chirality means the preferred direction of edge circulation in the synthetic optical lattice, not a violation of energy conservation or light travelling backward in time. [1]

The important experimental claim is access to continuously signed coupling inside a compact twisted-array architecture with two distinct classes of driven behavior. The accessible abstract does not establish insertion loss, optical operating wavelength, production yield, bandwidth or long-term stability for this implementation. Those are engineering requirements for a practical photonic component, not quantities to infer from a schematic. A theoretical analogy with electronic topological bands does not make this an electron transport measurement. [1]

The transferable principle is to treat interaction coefficients as programmable hardware. With nearly identical nodes, a graph of positive and negative links can support different collective modes depending on its coupling sequence. Photonic waveguides implement that graph by vector-field overlap; spin simulators and analog electronic networks use other mechanisms. Their dynamics may share an equation while their coherence, fabrication and noise constraints differ sharply. [1]

### Sources

1. [Gao et al., Nature Communications — Polarization-controlled Floquet engineering in twisted photonic lattices](https://www.nature.com/articles/s41467-026-78660-0) — 2026-10-15.

## Materials · Chemical vapor deposition — A liquid copper surface assembles bare niobium carbide films

A controlled Nb/C ratio and surface diffusion replace a conventional etching route for making few-layer Nb2C MXene.

Communications Materials study published 15 October 2026. Primary abstract and author list verified; complete temperature, thickness and yield tables not accessible.

MXenes are two-dimensional transition-metal carbides and nitrides. Traditionally, many are made by selectively etching layers from a thicker MAX-phase crystal. Etching can leave oxygen, fluorine or other surface termination groups, which change surface chemistry and electrical interfaces. A bare carbide sheet made directly by bottom-up synthesis is consequently not equivalent to the same sheet after a particular etch. The process matters because it determines both geometry and the exposed atomic boundary. [1]

Xinming Xing, Azra Khan and collaborators report surface-diffusion liquid-metal chemical vapor deposition, abbreviated SDLM-CVD. They use liquid copper as the growth surface for few-layer Nb2C. Conventional chemical vapor deposition introduces reactive species to a surface where adsorption, diffusion, reaction and nucleation compete. Here the local ratio of niobium to carbon on the molten Cu surface, and its spatial distribution, is central. A globally correct precursor ratio does not imply every location at the surface has the same ratio. [1]

With the appropriate local Nb/C conditions, the team obtained single-crystalline bare Nb2C flakes with trigonal symmetry. They also observed that growth could self-assemble into a continuous two-dimensional film. These are related but different successes: a separated crystal flake demonstrates local phase selection; a connected film addresses potential coverage and integration. Neither result alone establishes that the film can be transferred with no defects or meets the resistivity requirements of an electronic device. [1]

A minimal surface-balance description is partial_t c_i = D_i nabla^2 c_i + F_i - R_i, with c_i the surface concentration of element i, D_i its effective lateral diffusion coefficient, F_i its arriving flux and R_i its reaction or removal. This is an explanatory conservation model, not a fitted equation from the published report. It clarifies why local mobility and precursor supply determine the region in which correct stoichiometry persists long enough for crystal growth. [1]

Density-functional-theory calculations supplement the observations by evaluating candidate atomic configurations and interactions responsible for growth and coalescence. Such calculations can support a mechanism, but they do not measure every kinetic event in a working reactor. The abstract attributes the mechanistic interpretation to both observed growth and theoretical calculations. This distinction prevents turning a plausible atomic energy explanation into an unsupported claim of industrial process reproducibility. [1]

The paper does not supply, in the accessible abstract, verified values for furnace temperature, deposition throughput, wafer-scale area, defect density, film conductivity or operational device lifetime. The achieved synthesis is a proof of a directly grown niobium carbide system, not a qualified factory process. Its most reusable idea is that a liquid metal's lateral diffusion field can be engineered so a desired 2D composition appears locally and then coalesces. Extending that method to other MXenes still requires finding compatible phase diagrams and transfer methods. [1]

### Sources

1. [Xing et al., Communications Materials — Surface diffusion strategies for chemical vapor deposition of 2D Nb2C MXene films](https://www.nature.com/articles/s43246-026-01397-2) — 2026-10-15.

## ESP32 · Radio interfaces · Vision-controlled hardware — An ESP32-S3 lets a vision computer steer an existing pan-tilt head

A separate nRF24L01 link turns host movement requests into the controller's radio interface while retaining the original mechanics.

Hackaday project report published 15 October 2026. Linked Codeberg source was inaccessible; no uninspected driver protocol or performance claims are asserted.

To automatically follow an aircraft, a camera system must connect three physical coordinate systems: pixel coordinates in the observed frame, required optical pointing angles, and the electrical commands that a motorized head understands. A tempting but fragile approach is to equate a pixel error directly to a radio packet and hope that the mount reaches its intended position. Real tracking requires calibration, motion timing and a way of dealing with lost commands and motor inertia. [1]

Kyle Housley repurposed a Soonpho M7 pan-tilt camera head using an ESP32-S3 and an external nRF24L01 transceiver. The microcontroller accepts requests from a laptop through a serial connection. A second nRF24L01 installed in the original M7 controller receives movement commands, according to Hackaday. The bridge can request pan/tilt targets, smoother vector motion and shutter release. The nRF24L01 is a dedicated 2.4 GHz radio, not the ESP32-S3's built-in Wi-Fi radio pretending to be one. [1]

The laptop performs object detection using a YOLO-family computer vision model. Its output supplies image-plane positions for an aircraft target. This preserves a useful separation: expensive inference and image processing take place on a full computer, while the microcontroller owns the narrow protocol and radio bridge. Swapping the detector or even using ADS-B coordinates would not necessarily require replacing the microcontroller firmware if the serial control protocol remains stable. [1]

A small geometric example makes the calibration problem tangible. In a hypothetical camera with 40 degrees of horizontal field of view and an image width of 2000 pixels, a target displaced 100 pixels from the center implies a first-order pointing correction of roughly 40*100/2000 = 2 degrees. This is an illustrative calculation, not a value measured by Housley. Lens distortion, field-of-view changes with zoom, mechanical offsets and object motion all change the real response. [1]

The public description does not show whether a radio request is acknowledged by the head, whether the head reports its true measured angle, or how it handles communication loss. An absolute pointing command is not equivalent to an independently verified position. A safe controller should bound angular speed and define a stale-command response; those are general engineering constraints, not features confirmed for this build. The linked project repository on Codeberg could not be retrieved during this research, so packet formats, loop frequency and angular precision are not assigned invented numbers. [1]

What can be learned from the observed architecture is a way to reuse expensive mechanics without redesigning motors, gears and housings. The interface to the vision host is small and explicit, the radio connection is encapsulated, and the original camera head performs the physical actuation. The project is a useful protocol-bridge demonstration; precision tracking qualifications would require additional measurements. [1]

### Sources

1. [Zoe Skyforest, Hackaday — Building An M7 Pan Tilt Head Controller](https://hackaday.com/2026/10/15/building-an-m7-pan-tilt-head-controller/) — 2026-10-15.

## ESP32 · Hardware reverse engineering · Community project — A Motorola T900 pager gets a modern LoRa brain without losing its keyboard

A Heltec ESP32-S3 board replaces the internals while experimental probing restores the legacy LCD and QWERTY keyboard.

Hackaday published 14 October 2026, based on a builder report in r/meshtastic, not r/esp32. Current feature claims come from that project report and manufacturer specifications.

The Motorola T900 was designed as a two-way text pager with a physical QWERTY keyboard, an LCD and compact pocket hardware. The historical network is less useful today than those carefully fitted human-interface components. Salvaging the case is straightforward in concept; preserving the original keyboard and display is harder, because the electronics were never designed to present a documented interface to a contemporary microcontroller. Reusing them requires understanding the actual pin connections, voltage levels, scanning sequence and display drive before any messaging application can work. [1] [2]

The builder posting as zindustries87 reported probing and reverse engineering the T900 LCD and keyboard until both worked with a Heltec V4 development board. Their October demonstration used the original keyboard to send a Meshtastic message through an ESP32-S3-based prototype. That is progress in real hardware, but it is an author demonstration rather than independent reproduction, and the public post does not supply enough complete interface timing to certify any arbitrary T900 unit can be converted by following a simple pin list. [1] [2]

The Heltec WiFi LoRa 32 V4 combines the ESP32-S3R2 microcontroller with a separate Semtech SX1262 long-range radio. The processor provides application logic, Wi-Fi, BLE and peripheral interfaces; the SX1262 modulates and demodulates the sub-GHz LoRa transmission. Manufacturer descriptions include a configuration with 2 MB PSRAM and 16 MB external flash; the board and regional RF variant must still be confirmed. The important architecture fact is that LoRa is not a hidden radio mode inside the ESP32's Wi-Fi circuitry. [1] [3]

The practical recovery workflow begins by recording the untouched system: high-resolution PCB images, continuity tests of the keyboard flexible cable, measurements of idle voltage and capture of activity with a logic analyzer. If the keyboard is a passive matrix, selected row lines can be driven and column lines sampled with debouncing and ghost-key handling. If an integrated keyboard controller is present, the protocol may be entirely different. Similarly, an old LCD might need multiplex bias voltages or nonstandard segment timing, not the convenient SPI commands of a new e-paper or OLED module. None of those specific pin assignments can be responsibly inferred from a photograph. [1] [2]

On the software side, the underlying problem naturally separates into a keyboard event interface, display presentation layer and messaging transport. A decoded key event ought to have no knowledge of LoRa framing, and an incoming text message ought not depend on which LCD pin toggles to draw a glyph. This is a recommended decomposition derived from the task, not a claim that the demonstrator's unpublished firmware implements those exact abstractions. It is the separation that makes hardware substitution and future testing much easier. [1] [2]

The maker discusses potential Android-linked SMS, Wi-Fi messaging, vibration alerts, a rechargeable battery, improved illumination and games, but describes them as future or ongoing work rather than a completed feature matrix. Radio receive duty cycle, backlight load, LCD bias and deep-sleep wake behavior would be necessary to measure before claiming a useful battery life. Replacing the original supply with lithium also introduces charging, cutoff and thermal responsibilities that did not disappear because the enclosure fits the circuit. [1] [2]

The verified takeaway is hardware interface recovery: an old keypad and display are operating with a new ESP32-S3 and LoRa messaging path. The larger engineering principle is to reuse interfaces that were designed around people, while replacing the networking underneath. Complete source, display timing, RF compliance and current consumption remain unestablished from the accessible project material. A nice demonstration can be described accurately without pretending that every planned future feature already ships. [1] [2] [3]

### Sources

1. [Hackaday — Pager Converted To Meshtastic Node](https://hackaday.com/2026/10/14/pager-converted-to-meshtastic-node/) — 2026-10-14.

2. [zindustries87, r/meshtastic — Motorola T900 2-Way Pager Conversion](https://www.reddit.com/r/meshtastic/comments/1wyn3gm/motorola_t900_2way_pager_conversion/) — Undated reference; checked 2026-10-18.

3. [Heltec Documentation — WiFi LoRa 32 V4 hardware specifications](https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/) — Undated reference; checked 2026-10-18.

## ESP32 · USB HID · BLE · Closed-loop automation — An ESP32-S3 sends an iPhone its own screen so an agent can operate it

The new runtime eliminates the laptop by relaying compressed AirPlay over BLE to the same phone, then sending corrective USB mouse actions back.

Hackaday published 14 October 2026 describing the earlier runtime. GitHub README and commits inspected through 18 October 2026 00:06 UTC for the newer architecture; bandwidth figures are author reports.

An early version of Henry Yuan's ESP32 iPhone Agent used a laptop or desktop computer to receive an iPhone's AirPlay picture, a vision model to decide what to do, and a small ESP32-S3 board to send USB mouse and keyboard reports. Hackaday described that version on October 14. But the project's current README announces a different arrangement: the external computer has been removed from the runtime loop. The earlier UxPlay/Python system remains in the repository as tag v0.1.0, so the two variants should not be confused in reporting or benchmark comparisons. [1] [2]

In the revised system the ESP32-S3 establishes its own Wi-Fi access point and acts as an AirPlay receiver. The same iPhone being controlled mirrors its display to that access point, delivering compressed H.264 video. The board does not decode H.264 to full video frames: it forwards the compressed stream over Bluetooth Low Energy to a companion iPhone app. That app decodes the stream, submits selected screenshots to a compatible vision model, and runs a planner and actor that choose taps, swipes, drags, typing and navigation. BLE returns action commands to the board, whose native USB port appears as a keyboard and mouse. [1]

The signal loop is therefore iPhone display -> Wi-Fi AirPlay -> ESP32-S3 -> BLE -> iPhone application -> vision model -> BLE -> ESP32-S3 -> USB HID -> iPhone interface. It seems circuitous to send the phone its own pixels, but it permits external control through ordinary peripheral interfaces rather than modifying protected application internals. The project uses Apple's AssistiveTouch to translate mouse motion and clicking into actions on the display. This still does not reveal password fields, DRM video or other views omitted from screen mirroring. [1] [2]

BLE throughput explains the team's heavy reliance on compression. The README reports roughly 300 to 500 kilobits per second and a reduced mirrored picture of about 480 by 1040 pixels at no more than five frames a second. An uncompressed 24-bit RGB frame of that size contains 480×1040×24 = 11,980,800 bits, almost twelve megabits. At 500 kilobits per second, a single raw frame would consume nearly 24 seconds before packet overhead. Five uncompressed frames per second would require about 60 megabits per second. Keeping H.264 data compressed and accepting low frame rate are architectural necessities, not incidental quality settings. [1]

A second difficulty is the coordinate system. Standard USB HID mouse movement is relative; a vision model can request a tap at a position in screenshot pixels, but the board cannot simply issue an absolute OS-level tap through the mouse interface. The agent re-homes the pointer toward a corner, then searches for its displayed location and corrects before precise clicks. After each action it observes the next screen and checks whether the expected change occurred. That feedback loop is the difference between issuing plausible commands and actually measuring progress through a user interface. [1]

The documented target is a Seeed XIAO ESP32S3 board with native USB and PSRAM. Espressif's USB device documentation confirms that ESP32-S3 can present HID devices through its full-speed USB controller. USB Full Speed has a nominal signaling rate of 12 megabits per second, but that figure is a link specification, not a measured speed for the agent. The video path's reported hundreds of kilobits per second, the vision model's inference delay and any application's animation times are separate bottlenecks. The developer says each action step usually takes seconds, with model latency dominant. [1] [3]

The companion app runs on iOS 18 or later and still needs an Xcode build and installation once. During a run, the phone occupies its Wi-Fi connection with the ESP32 hotspot and uses cellular data to reach an external model. The project currently supports portrait calibration and ASCII keyboard input, and it documents inaccessible mirrored screens and stopped mirroring on device lock. Its own README acknowledges using a private iOS suspension API in a self-built app, an obstacle for normal App Store distribution. These limits do not negate the architecture; they define the conditions under which it has been demonstrated. [1]

The repository has continued changing after Hackaday's post. Its dated commits include documentation for exporting frame/action traces, a fix for an iOS MetricKit diagnostic crash and explicit model selection in setup by October 18 at 00:06 UTC. Exported traces enable a later engineer to reconstruct a failure from an observed frame, chosen action and resulting screen, rather than accepting a success anecdote. Bandwidth and runtime claims remain the developer's reports; no independent benchmark is asserted here. The transferable design is the separation of sensing, reasoning and actuation with observation after every significant action. [1] [2]

### Sources

1. [onehumanbeing, GitHub — ESP32 iPhone Agent: live README, code and release history](https://github.com/onehumanbeing/esp32-iphone-agent) — 2026-10-18.

2. [Zoe Skyforest, Hackaday — AI Controls iPhone Via ESP32](https://hackaday.com/2026/10/14/ai-controls-iphone-via-esp32/) — 2026-10-14.

3. [Espressif, ESP-USB programming guide — USB Device Stack on ESP32-S3](https://docs.espressif.com/projects/esp-usb/en/latest/esp32s3/usb_device.html) — Undated reference; checked 2026-10-18.
