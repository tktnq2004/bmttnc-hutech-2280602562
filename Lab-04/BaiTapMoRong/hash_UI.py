import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import hashlib

def blake2b_hex(data: bytes) -> str:
    h = hashlib.blake2b(digest_size=64)
    h.update(data)
    return h.hexdigest()

def md5_hex(data: bytes) -> str:
    h = hashlib.md5()
    h.update(data)
    return h.hexdigest()

def sha3_256_hex(data: bytes) -> str:
    h = hashlib.sha3_256()
    h.update(data)
    return h.hexdigest()

def sha256_hex(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()

class HashApp:
    def __init__(self, root):
        self.root = root
        root.title("Hash Toolkit — BLAKE2b / MD5 / SHA3-256 / SHA-256")
        root.geometry("760x520")
        root.resizable(False, False)

        main = ttk.Frame(root, padding=12)
        main.pack(fill=tk.BOTH, expand=True)

        label_in = ttk.Label(main, text="Input text (UTF-8):")
        label_in.grid(row=0, column=0, sticky="w")
        self.input_text = tk.Text(main, height=6, width=88, wrap="word")
        self.input_text.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(4,8))

        self.var_b2 = tk.BooleanVar(value=True)
        self.var_md5 = tk.BooleanVar(value=True)
        self.var_sha3 = tk.BooleanVar(value=True)
        self.var_sha256 = tk.BooleanVar(value=True)

        option_frame = ttk.Frame(main)
        option_frame.grid(row=2, column=0, columnspan=4, sticky="w", pady=(0,8))
        ttk.Checkbutton(option_frame, text="BLAKE2b (64 bytes)", variable=self.var_b2).pack(side="left", padx=6)
        ttk.Checkbutton(option_frame, text="MD5", variable=self.var_md5).pack(side="left", padx=6)
        ttk.Checkbutton(option_frame, text="SHA3-256", variable=self.var_sha3).pack(side="left", padx=6)
        ttk.Checkbutton(option_frame, text="SHA-256", variable=self.var_sha256).pack(side="left", padx=6)

        btn_frame = ttk.Frame(main)
        btn_frame.grid(row=3, column=0, columnspan=4, sticky="w", pady=(0,10))
        ttk.Button(btn_frame, text="Compute Selected", command=self.compute_selected).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Compute All", command=self.compute_all).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Clear", command=self.clear_all).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Save All to File...", command=self.save_all).pack(side="left", padx=6)

        row_base = 4
        self.result_vars = {
            "BLAKE2b": tk.StringVar(value=""),
            "MD5": tk.StringVar(value=""),
            "SHA3-256": tk.StringVar(value=""),
            "SHA-256": tk.StringVar(value=""),
        }

        self._make_result_row(main, row_base + 0, "BLAKE2b (64 bytes)", "BLAKE2b")
        self._make_result_row(main, row_base + 1, "MD5", "MD5")
        self._make_result_row(main, row_base + 2, "SHA3-256", "SHA3-256")
        self._make_result_row(main, row_base + 3, "SHA-256", "SHA-256")

        self.status = tk.StringVar(value="Ready.")
        status_label = ttk.Label(main, textvariable=self.status, relief="sunken", anchor="w")
        status_label.grid(row=row_base + 5, column=0, columnspan=4, sticky="we", pady=(12,0))

    def _make_result_row(self, parent, row, label_text, key):
        lbl = ttk.Label(parent, text=label_text + ":")
        lbl.grid(row=row, column=0, sticky="w", pady=6)
        ent = ttk.Entry(parent, textvariable=self.result_vars[key], width=88)
        ent.grid(row=row, column=1, columnspan=2, sticky="we", padx=(6,6))
        btn_copy = ttk.Button(parent, text="Copy", width=10, command=lambda k=key: self.copy_result(k))
        btn_copy.grid(row=row, column=3, sticky="e", padx=(0,6))

    def _get_input_bytes(self) -> bytes:
        txt = self.input_text.get("1.0", tk.END).rstrip("\n")
        if txt == "":
            return None
        return txt.encode("utf-8")

    def compute_selected(self):
        data = self._get_input_bytes()
        if data is None:
            messagebox.showwarning("Input required", "Please enter text to hash.")
            return
        if self.var_b2.get():
            self.result_vars["BLAKE2b"].set(blake2b_hex(data))
        if self.var_md5.get():
            self.result_vars["MD5"].set(md5_hex(data))
        if self.var_sha3.get():
            self.result_vars["SHA3-256"].set(sha3_256_hex(data))
        if self.var_sha256.get():
            self.result_vars["SHA-256"].set(sha256_hex(data))
        self.status.set("Computed selected hashes.")

    def compute_all(self):
        data = self._get_input_bytes()
        if data is None:
            messagebox.showwarning("Input required", "Please enter text to hash.")
            return
        self.result_vars["BLAKE2b"].set(blake2b_hex(data))
        self.result_vars["MD5"].set(md5_hex(data))
        self.result_vars["SHA3-256"].set(sha3_256_hex(data))
        self.result_vars["SHA-256"].set(sha256_hex(data))
        self.status.set("Computed all hashes.")

    def copy_result(self, key):
        val = self.result_vars[key].get()
        if not val:
            self.status.set(f"No value to copy for {key}.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(val)
        self.status.set(f"Copied {key} to clipboard.")

    def save_all(self):
        results = []
        for k, var in self.result_vars.items():
            v = var.get()
            if v:
                results.append(f"{k}: {v}")
        if not results:
            messagebox.showinfo("No results", "No computed hashes to save.")
            return
        default_name = "hashes.txt"
        path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name,
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("Input:\n")
                f.write(self.input_text.get("1.0", tk.END))
                f.write("\nResults:\n")
                f.write("\n".join(results))
            self.status.set(f"Saved results to: {path}")
            messagebox.showinfo("Saved", f"Results saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Save error", str(e))

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        for var in self.result_vars.values():
            var.set("")
        self.status.set("Cleared input and results.")

def main():
    root = tk.Tk()
    app = HashApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
