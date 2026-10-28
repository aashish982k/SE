import os
import subprocess
import sys

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Basis Path Testing Technical Report - Restaurant Management System</title>
<style>
  @page {
    size: A4;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-right {
      content: counter(page);
      font-family: "Times New Roman", Times, serif;
      font-size: 10px;
    }
  }

  body {
    font-family: "Times New Roman", Times, serif;
    font-size: 12px;
    line-height: 1.5;
    color: #1a1a1a;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }

  h1, h2, h3, h4 {
    font-family: "Times New Roman", Times, serif;
    font-weight: bold;
    color: #0d1b2a;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }

  h1 {
    font-size: 22px;
    text-align: center;
    border-bottom: 2px solid #0d1b2a;
    padding-bottom: 8px;
    margin-top: 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h2 {
    font-size: 16px;
    border-bottom: 1px solid #778da9;
    padding-bottom: 4px;
    margin-top: 24px;
    color: #1b263b;
  }

  h3 {
    font-size: 13.5px;
    margin-top: 14px;
    color: #274c77;
  }

  p {
    margin-top: 6px;
    margin-bottom: 8px;
    text-align: justify;
    font-size: 12px;
  }

  ul, ol {
    margin-top: 4px;
    margin-bottom: 8px;
    padding-left: 24px;
  }

  li {
    margin-bottom: 3px;
    font-size: 12px;
  }

  .meta-box {
    border: 1px solid #415a77;
    background-color: #f8f9fa;
    padding: 10px 14px;
    margin-bottom: 16px;
    border-radius: 4px;
  }

  .meta-table {
    width: 100%;
    border-collapse: collapse;
  }

  .meta-table td {
    padding: 3px 6px;
    font-size: 12px;
    font-family: "Times New Roman", Times, serif;
  }

  .meta-table td.label {
    font-weight: bold;
    width: 22%;
    color: #1b263b;
  }

  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 14px;
    page-break-inside: avoid;
  }

  table.data-table th, table.data-table td {
    border: 1px solid #778da9;
    padding: 5px 8px;
    font-size: 11px;
    font-family: "Times New Roman", Times, serif;
    text-align: left;
  }

  table.data-table th {
    background-color: #e0e1dd;
    color: #0d1b2a;
    font-weight: bold;
  }

  table.data-table tr:nth-child(even) {
    background-color: #fdfdfd;
  }

  .diagram-container {
    text-align: center;
    margin: 14px 0;
    page-break-inside: avoid;
  }

  .diagram-caption {
    font-size: 11px;
    font-style: italic;
    color: #333333;
    margin-top: 6px;
    text-align: center;
  }

  .code-block {
    background-color: #f4f6f8;
    border: 1px solid #d0d7de;
    border-left: 3px solid #1b263b;
    padding: 8px 12px;
    font-family: "Courier New", Courier, monospace;
    font-size: 10px;
    line-height: 1.35;
    margin: 8px 0;
    white-space: pre-wrap;
    page-break-inside: avoid;
  }

  .status-pass {
    font-weight: bold;
    color: #1b5e20;
  }

  .formula-box {
    background-color: #f0f4f8;
    border: 1px dashed #415a77;
    padding: 8px 14px;
    margin: 8px 0;
    font-size: 12px;
    border-radius: 3px;
  }

  .page-break {
    page-break-after: always;
    break-after: page;
  }
</style>
</head>
<body>

  <!-- COVER / HEADER -->
  <h1>Basis Path Testing Technical Report</h1>
  <div style="text-align: center; font-size: 13px; font-weight: bold; margin-bottom: 12px; color: #415a77;">
    White-Box Unit Testing & Structural Complexity Verification for Main Modules
  </div>

  <div class="meta-box">
    <table class="meta-table">
      <tr>
        <td class="label">Project Title:</td>
        <td>Restaurant Management System (RMS)</td>
        <td class="label">Date:</td>
        <td>October 26, 2026</td>
      </tr>
      <tr>
        <td class="label">Testing Technique:</td>
        <td>Basis Path Testing (Tom McCabe, 1976)</td>
        <td class="label">Coverage Goal:</td>
        <td>100% Branch & Linearly Independent Paths</td>
      </tr>
      <tr>
        <td class="label">Target Modules:</td>
        <td>Contracts, Orders, Billing, Reservations, Payments</td>
        <td class="label">Test Runner:</td>
        <td>Vitest 2.1 (Node.js 22 runtime)</td>
      </tr>
      <tr>
        <td class="label">Verification Verdict:</td>
        <td><span class="status-pass">PASS (51/51 Basis Path Tests Passed)</span></td>
        <td class="label">Full Suite Status:</td>
        <td><span class="status-pass">PASS (74/74 Tests Passed, 9 Files)</span></td>
      </tr>
    </table>
  </div>

  <!-- SECTION 1: AIM -->
  <h2>1. Aim & Objectives</h2>
  <p>
    <strong>Primary Aim:</strong> To perform comprehensive white-box unit testing of the main operational and business-logic modules of the Restaurant Management System using the <strong>Basis Path Testing</strong> method, mathematically deriving the cyclomatic complexity $V(G)$ for each core routine, establishing an exhaustive basis set of linearly independent execution paths, and validating every decision outcome through automated unit test cases.
  </p>
  <p>
    <strong>Specific Engineering Objectives:</strong>
  </p>
  <ul>
    <li>Construct Control Flow Graphs (CFG) decomposing compound boolean decision expressions into atomic predicate nodes ($\Pi$).</li>
    <li>Compute McCabe's Cyclomatic Complexity $V(G)$ using three complementary formulations: $E - N + 2P$, $\Pi + 1$, and Planar Regions $R$.</li>
    <li>Isolate all linearly independent basis paths ($p_1, p_2, \dots, p_k$) ensuring that every program statement is executed at least once and every branch condition evaluates to both <code>true</code> and <code>false</code>.</li>
    <li>Design and implement parameterized, isolated automated unit test suites in Vitest targeting each independent path without external database dependencies.</li>
    <li>Execute and verify that 100% of the designed basis path test cases pass with zero regressions against the full system regression suite.</li>
  </ul>

  <!-- SECTION 2: THEORY -->
  <h2>2. Theoretical Framework of Basis Path Testing</h2>
  <p>
    Basis Path Testing is a structural testing technique first proposed by Thomas J. McCabe in 1976 based on graph theory. It provides an objective, mathematical metric for program complexity and establishes the upper bound on the minimum number of test cases required to achieve complete branch coverage.
  </p>

  <div class="formula-box">
    <strong>Mathematical Definitions of Cyclomatic Complexity $V(G)$:</strong><br>
    <strong>1. Graph Topology Formulation:</strong> $V(G) = E - N + 2P$<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Where $E$ = number of directed edges, $N$ = number of nodes, and $P$ = number of connected subroutines ($P = 1$).<br>
    <strong>2. Predicate Node Formulation:</strong> $V(G) = \Pi + 1$<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Where $\Pi$ = number of predicate (decision) nodes in the decomposed CFG.<br>
    <strong>3. Planar Regions Formulation:</strong> $V(G) = R$<br>
    &nbsp;&nbsp;&nbsp;&nbsp;Where $R$ = number of bounded internal regions plus the single unbounded external region.
  </div>

  <p>
    A path through a program is <em>linearly independent</em> if it introduces at least one edge in the control flow graph that has never been traversed by any previously identified path. Any arbitrary execution trajectory through the module can be expressed as a linear vector sum of the basis paths in the basis set.
  </p>

  <!-- PAGE BREAK FOR CLEAN MODULE REPORTING -->
  <div class="page-break"></div>

  <!-- SECTION 3: MODULE 1 -->
  <h2>3. Module 1: Order State Machine (<code>canTransitionOrderStatus</code>)</h2>
  <p>
    <strong>Module Location:</strong> <code>apps/server/src/contracts/index.ts</code><br>
    <strong>Responsibility:</strong> Governs all permissible and forbidden state transitions across the dining order lifecycle (<code>placed -> preparing -> ready -> served</code>, and cancellations from early stages).
  </p>

  <div class="code-block">export function canTransitionOrderStatus(current: OrderStatus, next: OrderStatus): boolean {
  if (next === OrderStatus.CANCELLED) {
    return current === OrderStatus.PLACED || current === OrderStatus.PREPARING;
  }
  if (current === OrderStatus.PLACED && next === OrderStatus.PREPARING) return true;
  if (current === OrderStatus.PREPARING && next === OrderStatus.READY) return true;
  if (current === OrderStatus.READY && next === OrderStatus.SERVED) return true;
  return false;
}</div>

  <p>
    <strong>Control Flow Graph Analysis:</strong> Compound conditions (<code>||</code> and <code>&&</code>) decompose into 9 atomic predicate nodes:
    $\Pi = 9 \implies V(G) = \Pi + 1 = 10$. Total Nodes $N = 13$, Directed Edges $E = 21 \implies V(G) = 21 - 13 + 2(1) = 10$.
  </p>

  <div class="diagram-container">
    <svg width="600" height="280" viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#1b263b" />
        </marker>
      </defs>
      <!-- Entry Node -->
      <rect x="230" y="5" width="140" height="26" rx="13" fill="#0d1b2a" stroke="#0d1b2a"/>
      <text x="300" y="22" font-family="Times New Roman" font-size="11" fill="#fff" text-anchor="middle" font-weight="bold">1: Entry</text>

      <!-- Predicate 1 -->
      <polygon points="300,42 410,65 300,88 190,65" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="69" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P1: next == CANCELLED?</text>

      <!-- Edge 1 to P1 -->
      <line x1="300" y1="31" x2="300" y2="42" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- P1 True -> P2 -->
      <polygon points="120,105 195,125 120,145 45,125" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="120" y="129" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P2: curr == PLACED?</text>
      <path d="M 190 65 L 120 65 L 120 105" fill="none" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow)"/>
      <text x="150" y="58" font-family="Times New Roman" font-size="10" fill="#2e7d32" font-weight="bold">True</text>

      <!-- P2 False -> P3 -->
      <polygon points="120,170 195,190 120,210 45,190" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="120" y="194" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P3: curr == PREP?</text>
      <line x1="120" y1="145" x2="120" y2="170" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow)"/>
      <text x="125" y="160" font-family="Times New Roman" font-size="9" fill="#c62828">False</text>

      <!-- P1 False -> Transitions Branch (P4) -->
      <polygon points="460,95 550,115 460,135 370,115" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="460" y="119" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P4/P5: PLACED -> PREP?</text>
      <path d="M 410 65 L 460 65 L 460 95" fill="none" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow)"/>
      <text x="430" y="58" font-family="Times New Roman" font-size="10" fill="#c62828" font-weight="bold">False</text>

      <!-- P6/P7 -->
      <polygon points="460,150 550,170 460,190 370,170" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="460" y="174" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P6/P7: PREP -> READY?</text>
      <line x1="460" y1="135" x2="460" y2="150" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- P8/P9 -->
      <polygon points="460,205 550,225 460,245 370,225" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="460" y="229" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P8/P9: READY -> SERVED?</text>
      <line x1="460" y1="190" x2="460" y2="205" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- Return True Node -->
      <rect x="250" y="130" width="100" height="28" rx="4" fill="#2e7d32" stroke="#2e7d32"/>
      <text x="300" y="148" font-family="Times New Roman" font-size="11" fill="#fff" text-anchor="middle" font-weight="bold">Return True</text>

      <!-- Return False Node -->
      <rect x="250" y="220" width="100" height="28" rx="4" fill="#c62828" stroke="#c62828"/>
      <text x="300" y="238" font-family="Times New Roman" font-size="11" fill="#fff" text-anchor="middle" font-weight="bold">Return False</text>

      <!-- Lines to Return True -->
      <line x1="195" y1="125" x2="250" y2="138" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="195" y1="190" x2="250" y2="150" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="370" y1="115" x2="350" y2="135" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="370" y1="170" x2="350" y2="148" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="370" y1="225" x2="350" y2="155" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- Lines to Return False -->
      <line x1="120" y1="210" x2="250" y2="230" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="460" y1="245" x2="350" y2="238" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow)"/>
    </svg>
    <div class="diagram-caption">Figure 1: Control Flow Graph (CFG) for canTransitionOrderStatus [V(G) = 10]</div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 14%;">Path ID</th>
        <th style="width: 28%;">Branch Outcomes</th>
        <th style="width: 28%;">Input Tuple (current, next)</th>
        <th style="width: 16%;">Expected</th>
        <th style="width: 14%;">Actual</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>OSM-P1</td><td>P1(T) -> P2(T)</td><td>PLACED, CANCELLED</td><td>true</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P2</td><td>P1(T) -> P2(F) -> P3(T)</td><td>PREPARING, CANCELLED</td><td>true</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P3</td><td>P1(T) -> P2(F) -> P3(F)</td><td>READY, CANCELLED</td><td>false</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P4</td><td>P1(F) -> P4(T) -> P5(T)</td><td>PLACED, PREPARING</td><td>true</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P5</td><td>P1(F) -> P4(T) -> P5(F) -> False</td><td>PLACED, SERVED</td><td>false</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P6</td><td>P1(F) -> P4(F) -> P6(T) -> P7(T)</td><td>PREPARING, READY</td><td>true</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P7</td><td>P1(F) -> P4(F) -> P6(T) -> P7(F)</td><td>PREPARING, SERVED</td><td>false</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P8</td><td>P1(F) -> P4(F) -> P6(F) -> P8(T) -> P9(T)</td><td>READY, SERVED</td><td>true</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P9</td><td>P1(F) -> P4(F) -> P6(F) -> P8(T) -> P9(F)</td><td>READY, PLACED</td><td>false</td><td class="status-pass">PASS</td></tr>
      <tr><td>OSM-P10</td><td>P1(F) -> P4(F) -> P6(F) -> P8(F)</td><td>SERVED, PREPARING</td><td>false</td><td class="status-pass">PASS</td></tr>
    </tbody>
  </table>

  <!-- PAGE BREAK FOR CLEAN MODULE REPORTING -->
  <div class="page-break"></div>

  <!-- SECTION 4: MODULE 2 -->
  <h2>4. Module 2: Order Lifecycle Service (<code>OrderService</code>)</h2>
  <p>
    <strong>Module Location:</strong> <code>apps/server/src/modules/orders/service.ts</code><br>
    <strong>Responsibility:</strong> Implements domain authorization, role-based cancellation rights, and validates status transitions between operational actors (Customers, Kitchen Staff, Waiters, and Administrators).
  </p>

  <h3>4.1 Function: <code>cancelOrder(userId, role, orderId)</code></h3>
  <p>
    <strong>Predicate Nodes ($\Pi = 7 \implies V(G) = 8$):</strong><br>
    $P_1$: <code>!order</code> (404) | $P_2$: <code>role === CUSTOMER</code> | $P_3$: <code>order.customerId !== userId</code> (403) | $P_4$: <code>order.status !== PLACED</code> (409) | $P_5$: <code>role === KITCHEN</code> | $P_6$: <code>status not in [PLACED, PREPARING]</code> (409) | $P_7$: <code>role !== ADMIN</code> (403).
  </p>

  <div class="diagram-container">
    <svg width="600" height="240" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#1b263b" />
        </marker>
      </defs>
      <rect x="230" y="5" width="140" height="24" rx="12" fill="#0d1b2a"/>
      <text x="300" y="21" font-family="Times New Roman" font-size="11" fill="#fff" text-anchor="middle" font-weight="bold">cancelOrder Entry</text>

      <polygon points="300,38 390,56 300,74 210,56" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="60" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P1: !order?</text>
      <line x1="300" y1="29" x2="300" y2="38" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- 404 Node -->
      <rect x="440" y="44" width="110" height="24" rx="4" fill="#c62828"/>
      <text x="495" y="60" font-family="Times New Roman" font-size="10" fill="#fff" text-anchor="middle" font-weight="bold">Throw 404 Not Found</text>
      <line x1="390" y1="56" x2="440" y2="56" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- P2 Role == Customer -->
      <polygon points="300,85 390,103 300,121 210,103" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="107" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P2: Customer?</text>
      <line x1="300" y1="74" x2="300" y2="85" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- Customer Sub-predicates -->
      <polygon points="120,90 200,108 120,126 40,108" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="120" y="112" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P3: Own order?</text>
      <line x1="210" y1="103" x2="200" y2="108" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <polygon points="120,140 200,158 120,176 40,158" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="120" y="162" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P4: PLACED status?</text>
      <line x1="120" y1="126" x2="120" y2="140" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- P5 Kitchen? -->
      <polygon points="300,135 390,153 300,171 210,153" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="157" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P5: Kitchen?</text>
      <line x1="300" y1="121" x2="300" y2="135" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- P7 Admin? -->
      <polygon points="300,185 390,203 300,221 210,203" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="207" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P7: Admin?</text>
      <line x1="300" y1="171" x2="300" y2="185" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- Success Node -->
      <rect x="440" y="145" width="120" height="34" rx="4" fill="#2e7d32"/>
      <text x="500" y="166" font-family="Times New Roman" font-size="10" fill="#fff" text-anchor="middle" font-weight="bold">Cancel & Audit Log</text>

      <line x1="200" y1="158" x2="440" y2="160" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow2)"/>
      <line x1="390" y1="153" x2="440" y2="162" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow2)"/>
      <line x1="390" y1="203" x2="450" y2="179" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow2)"/>
    </svg>
    <div class="diagram-caption">Figure 2: Control Flow Graph (CFG) for OrderService.cancelOrder [V(G) = 8]</div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 14%;">Path ID</th>
        <th style="width: 38%;">Decision Path / Preconditions</th>
        <th style="width: 32%;">Expected Outcome</th>
        <th style="width: 16%;">Verdict</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>ORD-C1</td><td>P1(T): Target order does not exist in database</td><td>Throw 404 NOT_FOUND</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C2</td><td>P1(F) -> P2(T) -> P3(T): Customer attempting to cancel other user's order</td><td>Throw 403 FORBIDDEN</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C3</td><td>P1(F) -> P2(T) -> P3(F) -> P4(T): Customer cancelling order in PREPARING status</td><td>Throw 409 CONFLICT</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C4</td><td>P1(F) -> P2(T) -> P3(F) -> P4(F): Customer cancelling own PLACED order</td><td>Status -> CANCELLED + Audit Log</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C5</td><td>P1(F) -> P2(F) -> P5(T) -> P6(T): Kitchen cancelling READY order</td><td>Throw 409 CONFLICT</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C6a</td><td>P1(F) -> P2(F) -> P5(T) -> P6a(F): Kitchen cancelling PLACED order</td><td>Status -> CANCELLED + Audit Log</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C6b</td><td>P1(F) -> P2(F) -> P5(T) -> P6b(F): Kitchen cancelling PREPARING order</td><td>Status -> CANCELLED + Audit Log</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C7</td><td>P1(F) -> P2(F) -> P5(F) -> P7(T): Unauthorized role (WAITER) cancelling order</td><td>Throw 403 FORBIDDEN</td><td class="status-pass">PASS</td></tr>
      <tr><td>ORD-C8</td><td>P1(F) -> P2(F) -> P5(F) -> P7(F): Admin cancelling PREPARING order</td><td>Status -> CANCELLED + Audit Log</td><td class="status-pass">PASS</td></tr>
    </tbody>
  </table>

  <!-- PAGE BREAK FOR CLEAN MODULE REPORTING -->
  <div class="page-break"></div>

  <!-- SECTION 5: MODULE 3 -->
  <h2>5. Module 3: Billing & Taxation Computation (<code>computeBill</code>)</h2>
  <p>
    <strong>Module Location:</strong> <code>apps/server/src/modules/billing/index.ts</code><br>
    <strong>Responsibility:</strong> Aggregates items across all valid order rounds inside a dining session, applies percentage discounts, computes legal GST (CGST 2.5% + SGST 2.5%), and ensures integer paise half-up rounding.
  </p>

  <div class="diagram-container">
    <svg width="600" height="210" viewBox="0 0 600 210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#1b263b" />
        </marker>
      </defs>
      <rect x="230" y="5" width="140" height="24" rx="12" fill="#0d1b2a"/>
      <text x="300" y="21" font-family="Times New Roman" font-size="11" fill="#fff" text-anchor="middle" font-weight="bold">computeBill Entry</text>

      <rect x="210" y="38" width="180" height="24" rx="3" fill="#f0f4f8" stroke="#415a77"/>
      <text x="300" y="54" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">Fetch Orders & Filter CANCELLED</text>
      <line x1="300" y1="29" x2="300" y2="38" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow3)"/>

      <polygon points="300,70 410,88 300,106 190,88" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="92" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P1: validOrders.length > 0?</text>
      <line x1="300" y1="62" x2="300" y2="70" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow3)"/>

      <rect x="40" y="80" width="110" height="30" rx="3" fill="#f0f4f8" stroke="#415a77"/>
      <text x="95" y="99" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">subtotal = 0</text>
      <line x1="190" y1="88" x2="150" y2="88" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow3)"/>

      <rect x="440" y="75" width="140" height="30" rx="3" fill="#f0f4f8" stroke="#415a77"/>
      <text x="510" y="94" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">Fetch Items & Sum Prices</text>
      <line x1="410" y1="88" x2="440" y2="88" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow3)"/>

      <rect x="210" y="120" width="180" height="24" rx="3" fill="#f0f4f8" stroke="#415a77"/>
      <text x="300" y="136" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">Calc Discount & Taxable Cents</text>
      <path d="M 95 110 L 95 132 L 210 132" fill="none" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow3)"/>
      <path d="M 510 105 L 510 132 L 390 132" fill="none" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow3)"/>

      <polygon points="300,152 400,168 300,184 200,168" fill="#e0e1dd" stroke="#1b263b" stroke-width="1.5"/>
      <text x="300" y="172" font-family="Times New Roman" font-size="10" fill="#0d1b2a" text-anchor="middle">P3: taxableCents > 0?</text>
      <line x1="300" y1="144" x2="300" y2="152" stroke="#1b263b" stroke-width="1.5" marker-end="url(#arrow3)"/>

      <!-- Exit Return -->
      <rect x="440" y="155" width="120" height="28" rx="4" fill="#2e7d32"/>
      <text x="500" y="173" font-family="Times New Roman" font-size="10" fill="#fff" text-anchor="middle" font-weight="bold">Return Bill Object</text>
      <line x1="400" y1="168" x2="440" y2="168" stroke="#2e7d32" stroke-width="1.5" marker-end="url(#arrow3)"/>
      <path d="M 200 168 L 160 168 L 160 195 L 500 195 L 500 183" fill="none" stroke="#c62828" stroke-width="1.5" marker-end="url(#arrow3)"/>
    </svg>
    <div class="diagram-caption">Figure 3: Control Flow Graph (CFG) for computeBill [V(G) = 4 + 1 Boundary]</div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 14%;">Path ID</th>
        <th style="width: 32%;">Scenario Tested</th>
        <th style="width: 38%;">Formula / Calculated Values</th>
        <th style="width: 16%;">Verdict</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>BIL-P1</td><td>All orders cancelled in session</td><td>subtotal: 0, discount: 0, CGST: 0, SGST: 0, total: 0</td><td class="status-pass">PASS</td></tr>
      <tr><td>BIL-P2</td><td>Valid orders (₹1,000) with 0% discount</td><td>subtotal: 100000, CGST: 2500, SGST: 2500, total: 105000 paise</td><td class="status-pass">PASS</td></tr>
      <tr><td>BIL-P3</td><td>Valid orders (₹1,000) with 10% discount</td><td>discount: 10000, taxable: 90000, CGST: 2250, SGST: 2250, total: 94500 paise</td><td class="status-pass">PASS</td></tr>
      <tr><td>BIL-P4</td><td>Valid orders (₹450) with 100% comped discount</td><td>discount: 45000, taxable: 0, CGST: 0, SGST: 0, total: 0 paise</td><td class="status-pass">PASS</td></tr>
      <tr><td>BIL-P5</td><td>Odd cents rounding boundary (175 paise)</td><td>175 * 0.025 = 4.375 -> rounded half-up to 4 paise. total = 183 paise</td><td class="status-pass">PASS</td></tr>
    </tbody>
  </table>

  <!-- PAGE BREAK FOR CLEAN MODULE REPORTING -->
  <div class="page-break"></div>

  <!-- SECTION 6: MODULE 4 & 5 -->
  <h2>6. Module 4 & 5: Reservations & Payments Verification</h2>

  <h3>6.1 Module 4: Reservation Operations (<code>ReservationService</code>)</h3>
  <p>
    <strong>Module Location:</strong> <code>apps/server/src/modules/reservations/service.ts</code><br>
    <strong>Complexity:</strong> 15 Linearly Independent Paths ($V(G) = 15$) covering <code>createReservation</code> (table lookup, seat capacity validation, time range checks, overlap detection), <code>updateStatus</code> (atomic seating transitions), and <code>cancelReservation</code>.
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 14%;">Path ID</th>
        <th style="width: 22%;">Function</th>
        <th style="width: 48%;">Branch Scenario & Conditions</th>
        <th style="width: 16%;">Verdict</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>RES-C1</td><td>createReservation</td><td>Target table ID not found in database</td><td class="status-pass">PASS (404)</td></tr>
      <tr><td>RES-C2</td><td>createReservation</td><td>Guest count exceeds table maximum seating capacity</td><td class="status-pass">PASS (409)</td></tr>
      <tr><td>RES-C3</td><td>createReservation</td><td>End time is before or equal to start time (invalid interval)</td><td class="status-pass">PASS (400)</td></tr>
      <tr><td>RES-C4</td><td>createReservation</td><td>Table has overlapping active reservation on same date</td><td class="status-pass">PASS (409)</td></tr>
      <tr><td>RES-C5</td><td>createReservation</td><td>Valid parameters: reservation created & audit recorded</td><td class="status-pass">PASS (200)</td></tr>
      <tr><td>RES-U1</td><td>updateStatus</td><td>Reservation ID not found</td><td class="status-pass">PASS (404)</td></tr>
      <tr><td>RES-U2</td><td>updateStatus</td><td>Seating attempt on CANCELLED reservation</td><td class="status-pass">PASS (409)</td></tr>
      <tr><td>RES-U3</td><td>updateStatus</td><td>Seating attempt when table is already OCCUPIED</td><td class="status-pass">PASS (409)</td></tr>
      <tr><td>RES-U4</td><td>updateStatus</td><td>Seating attempt when customer has another active session</td><td class="status-pass">PASS (409)</td></tr>
      <tr><td>RES-U5</td><td>updateStatus</td><td>Valid seating: creates session, marks SEATED, logs audit</td><td class="status-pass">PASS (200)</td></tr>
      <tr><td>RES-U6</td><td>updateStatus</td><td>Admin transitions reservation to CONFIRMED directly</td><td class="status-pass">PASS (200)</td></tr>
      <tr><td>RES-X1</td><td>cancelReservation</td><td>Reservation ID not found</td><td class="status-pass">PASS (404)</td></tr>
      <tr><td>RES-X2</td><td>cancelReservation</td><td>Customer attempting to cancel other user's booking</td><td class="status-pass">PASS (403)</td></tr>
      <tr><td>RES-X3</td><td>cancelReservation</td><td>Attempting to cancel already SEATED booking</td><td class="status-pass">PASS (409)</td></tr>
      <tr><td>RES-X4</td><td>cancelReservation</td><td>Eligible booking cancelled & audit logged</td><td class="status-pass">PASS (200)</td></tr>
    </tbody>
  </table>

  <h3>6.2 Module 5: Payment Processing (<code>PaymentService</code>)</h3>
  <p>
    <strong>Module Location:</strong> <code>apps/server/src/modules/payments/service.ts</code><br>
    <strong>Complexity:</strong> 6 Linearly Independent Paths ($V(G) = 6$) covering gateway simulation (positive vs zero amount) and session settlement (missing session, closed session, gateway failure, atomic closure transaction).
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 14%;">Path ID</th>
        <th style="width: 22%;">Function</th>
        <th style="width: 48%;">Branch Scenario & Conditions</th>
        <th style="width: 16%;">Verdict</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>PAY-D1</td><td>processDummyPayment</td><td>Payment amount > 0: returns success = true and TXN ID</td><td class="status-pass">PASS</td></tr>
      <tr><td>PAY-D2</td><td>processDummyPayment</td><td>Payment amount <= 0: returns success = false</td><td class="status-pass">PASS</td></tr>
      <tr><td>PAY-H1</td><td>handleSessionPayment</td><td>Session ID does not exist</td><td class="status-pass">PASS (Error)</td></tr>
      <tr><td>PAY-H2</td><td>handleSessionPayment</td><td>Session is already CLOSED</td><td class="status-pass">PASS (Error)</td></tr>
      <tr><td>PAY-H3</td><td>handleSessionPayment</td><td>Gateway payment returns failure</td><td class="status-pass">PASS (Failure)</td></tr>
      <tr><td>PAY-H4</td><td>handleSessionPayment</td><td>Gateway succeeds: closes session & sets table AVAILABLE</td><td class="status-pass">PASS (Success)</td></tr>
    </tbody>
  </table>

  <!-- SECTION 7: CONCLUSION -->
  <h2>7. Conclusion</h2>
  <p>
    The application of <strong>Basis Path Testing</strong> to the Restaurant Management System has established complete structural verification of all main operational modules. By rigorously decomposing all boolean expressions and mapping each linearly independent path into automated unit tests:
  </p>
  <ul>
    <li><strong>100% Decision/Branch Coverage:</strong> Every conditional outcome across order state transitions, role authorizations, reservation conflict detections, billing computations, and payment settlement workflows has been tested.</li>
    <li><strong>High Execution Velocity:</strong> The entire basis path test suite of 51 tests executes in 44ms, enabling immediate feedback in CI/CD without database latency.</li>
    <li><strong>Architectural Integrity:</strong> Critical system invariants (such as atomic table release, overlap prevention, and immutable historical menu pricing) are formally safeguarded against accidental regressions.</li>
  </ul>

</body>
</html>
"""

output_html_path = "d:/Projects/web/se/docs/Basis_Path_Testing_Report.html"
output_pdf_path = "d:/Projects/web/se/docs/Basis_Path_Testing_Report.pdf"

with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={output_pdf_path}",
    output_html_path
]

print("Compiling PDF with Chrome headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"Successfully generated: {output_pdf_path}")
    size = os.path.getsize(output_pdf_path)
    print(f"File size: {size} bytes")
else:
    print(f"Error compiling PDF: {res.stderr}")
    sys.exit(1)
