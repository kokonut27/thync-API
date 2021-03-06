CSS = """!!syntax!!.replit-ui-theme-root.dark{!!css!!}.replit-ui-theme-root.light{!!css!!}.line-numbers {color: var(--color-primary-1) !important;}.jsx-3971054001.content, p, .jsx-4279741890 {background-color: var(--color-background-2) !important;color: #fff !important;}.jsx-3414412928 {background-color: var(--color-background-1) !important;}.toggle-bar {background-color: var(--color-foreground-2) !important;}.jsx-467725132 {background-color: var(--color-background-3) !important;}.jsx-2906438576, .jsx-986859180, .jsx-918008940  {background-color: var(--color-background-3) !important;}.interactive.jsx-2106077415:hover {border-color: var(--color-background-4) !important;}.jsx-3414412928.sidebar-layout-header-toggle-alert {background-color: var(--color-primary-1) !important;}"""

JS = """javascript:(function() {let theme = document.getElementById("thync-theme");let display = document.getElementById("thync-display");if (theme && display) {var go = confirm("Are you sure you want to switch Replit themes?");if (go) {theme.remove();display.remove();alert("This Replit theme has been stopped.");}} else {var go = confirm("Run this thync theme?\\n\\nName: !name!\\nDescription: !description!");if (go) {var style = document.createElement("style");var head = document.getElementsByTagName("head")[0];var target = document.getElementsByClassName("jsx-2607100739")[0];style.setAttribute("id", "thync-theme");style.appendChild(document.createTextNode(`!css!`));if (target) {target.insertAdjacentHTML("afterend", `<a id="thync-display" class="jsx-2607100739" target="_blank" href="//github.com/JBYT27/thync"><span class="jsx-2607100739 sidebar-layout-nav-item-icon"><img src="https://www.pngkey.com/png/full/117-1175359_graphic-transparent-internet-clipart-cloud-computing-does-cloud.png" alt="cloud images" height="95%" width="95%"/></span><div class="jsx-2607100739">thync</div><div class="jsx-2607100739 beta-label"><div style="background-color: #6262ff;" class="jsx-4210545632 beta-tag">ON</div></div></a>`);} else {alert("thync badge could not be applied.");}head.appendChild(style);alert("thync has been turned on!");} else {alert("thync has been cancelled.");}}})();"""

# Dark: `javascript:(function() {document.body.className = "replit-ui-theme-root dark"})();`
# Light: `javascript:(function() {document.body.className = "replit-ui-theme-root light")();`

BASE_TOKENS = [f"span.mtk{n}" for n in range(8)]

TOKENS = [
    "keyword",
    "string",
    "comment",
    "variable",
    "punctuation",
    "constant.other",
    "constant.language",
    "constant.numeric",
    "parameter.variable",
    "function.support",
    "storage.type",
    "paren.rparen",
    "lparen.paren"
]

DEFAULT = {
    "name": "Light Theme",
    "description": "Default theme for Replit",
    "default": "light"
}

COLORS = {
    "dark": {
        "background-1": "#1d2333",
        "background-2": "#171d2d",
        "background-3": "#0e1525",
        "control-1": "#313646",
        "control-2": "#2b3140",
        "control-3": "#262b3b",
        "border": "#313646",
        "foreground-1": "#e1e2e4",
        "foreground-2": "#90939c",
        "foreground-3": "#696d78",
        "foreground-4": "#4e525f",
        "foreground-transparent-1": "rgba(14, 21, 37, 0.48)",
        "foreground-transparent-2": "rgba(14, 21, 37, 0.24)",
        "foreground-transparent-3": "rgba(14, 21, 37, 0.12)",
        "primary-1": "#3485e4",
        "primary-2": "#337bd2",
        "primary-3": "#3273c4",
        "primary-4": "#316cb8",
        "primary-transparent-1": "rgba(52, 133, 228, 0.48)",
        "primary-transparent-2": "rgba(52, 133, 228, 0.24)",
        "primary-transparent-3": "rgba(52, 133, 228, 0.12)",
        "negative-1": "#ff491c",
        "negative-2": "#eb451b",
        "negative-3": "#db411b",
        "negative-4": "#cd3e1a",
        "negative-transparent-1": "rgba(255, 73, 28, 0.48)",
        "negative-transparent-2": "rgba(255, 73, 28, 0.24)",
        "negative-transparent-3": "rgba(255, 73, 28, 0.12)",
        "warning-1": "#f26702",
        "warning-2": "#de5f07",
        "warning-3": "#ce590a",
        "warning-4": "#c0540c",
        "warning-transparent-1": "rgba(242, 103, 2, 0.48)",
        "warning-transparent-2": "rgba(242, 103, 2, 0.24)",
        "warning-transparent-3": "rgba(242, 103, 2, 0.12)",
        "positive-1": "#20ab46",
        "positive-2": "#219d41",
        "positive-3": "#22923d",
        "positive-4": "#22883a",
        "positive-transparent-1": "rgba(24, 204, 81, 0.48)",
        "positive-transparent-2": "rgba(24, 204, 81, 0.24)",
        "positive-transparent-3": "rgba(24, 204, 81, 0.12)"
    },
    "light": {
        "background-1": "#ffffff",
        "background-2": "#f6f6f6",
        "background-3": "#eeeeee",
        "control-1": "#e0e0e0",
        "control-2": "#e9e9e9",
        "control-3": "#f3f3f3",
        "border": "#e0e0e0",
        "foreground-1": "#363636",
        "foreground-2": "#6f6f6f",
        "foreground-3": "#949494",
        "foreground-4": "#b7b7b7",
        "foreground-transparent-1": "rgba(255, 255, 255, 0.48)",
        "foreground-transparent-2": "rgba(255, 255, 255, 0.24)",
        "foreground-transparent-3": "rgba(255, 255, 255, 0.12)",
        "primary-1": "#3485e4",
        "primary-2": "#337ad1",
        "primary-3": "#3272c2",
        "primary-4": "#316ab4",
        "primary-transparent-1": "rgba(52, 133, 228, 0.48)",
        "primary-transparent-2": "rgba(52, 133, 228, 0.24)",
        "primary-transparent-3": "rgba(52, 133, 228, 0.12)",
        "negative-1": "#ff491c",
        "negative-2": "#e9441b",
        "negative-3": "#d8411b",
        "negative-4": "#c93d1a",
        "negative-transparent-1": "rgba(255, 73, 28, 0.48)",
        "negative-transparent-2": "rgba(255, 73, 28, 0.24)",
        "negative-transparent-3": "rgba(255, 73, 28, 0.12)",
        "warning-1": "#eb6404",
        "warning-2": "#d65c08",
        "warning-3": "#c7560b",
        "warning-4": "#b8510d",
        "warning-transparent-1": "rgba(242, 103, 2, 0.48)",
        "warning-transparent-2": "rgba(242, 103, 2, 0.24)",
        "warning-transparent-3": "rgba(242, 103, 2, 0.12)",
        "positive-1": "#21a243",
        "positive-2": "#21953e",
        "positive-3": "#228a3a",
        "positive-4": "#228037",
        "positive-transparent-1": "rgba(24, 204, 81, 0.48)",
        "positive-transparent-2": "rgba(24, 204, 81, 0.24)",
        "positive-transparent-3": "rgba(24, 204, 81, 0.12)"
    },

    "code": """"""
}