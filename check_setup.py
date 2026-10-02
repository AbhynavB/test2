import os
import sys

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
ok = True


def check(label, passed, hint=""):
    global ok
    print(("PASS  " if passed else "FAIL  ") + label + ("" if passed else "  ->  " + hint))
    ok = ok and bool(passed)


check("Python 3.10 or newer", sys.version_info >= (3, 10), "wrong Python version")
try:
    import openai, streamlit  # noqa: F401
    check("openai and streamlit installed", True)
except ImportError as e:
    check("openai and streamlit installed", False, str(e))

key = os.environ.get("GEMINI_API_KEY")
check("GEMINI_API_KEY is set", bool(key), "add your key as a secret, then restart")

if ok:
    from openai import OpenAI
    try:
        client = OpenAI(api_key=key, base_url=BASE_URL)
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Reply with only the word READY"}],
        )
        check("Gemini API call works", "READY" in r.choices[0].message.content.upper())
    except Exception as e:
        check("Gemini API call works", False, str(e)[:150])

print("\nALL GOOD - you're ready for class!" if ok
      else "\nSomething needs fixing - send a screenshot to your teacher.")
