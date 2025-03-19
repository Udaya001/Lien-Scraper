from scrapper.lien_scrapper import LienScraper

if __name__ == "__main__":
    base_url = "https://yumacountyaz-recweb.tylerhost.net"
    scrapper = LienScraper(base_url)

    if scrapper.login():
        print("[+] Login successful!")

        if scrapper.search(start_date="01/01/2024", end_date="12/31/2024"):
            print("[+] Search completed successfully!")

            document_links = scrapper.get_search_results()  # Extract unique & working links
            if document_links:
                print(f"[+] Found {len(document_links)} document links! Processing now...")

                # Process each document: Extract text & download PDFs
                scrapper.process_documents(document_links)

                print("[✔] All documents processed successfully!")
            else:
                print("[-] No working document links found.")
        else:
            print("[-] Search failed, skipping document processing.")
    else:
        print("[-] Login failed, exiting script.")
