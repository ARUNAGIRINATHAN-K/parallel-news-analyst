import langchain
import pkgutil

print(f"LangChain version: {langchain.__version__}")
print(f"LangChain path: {langchain.__path__}")

def list_submodules(package):
    if hasattr(package, "__path__"):
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
            print(f"Submodule: {modname}")

print("--- LangChain Submodules ---")
list_submodules(langchain)

try:
    import langchain_community
    print("--- LangChain Community Submodules ---")
    list_submodules(langchain_community)
except ImportError:
    print("langchain_community not installed")

import langchain_community.chains
print(dir(langchain_community.chains))
