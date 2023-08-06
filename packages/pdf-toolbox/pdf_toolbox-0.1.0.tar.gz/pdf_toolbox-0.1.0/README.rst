===========
PDF TOOLBOX
===========

This package is designed to be used as an extensible library.

**PDF TOOLBOX allows extracting, parsing, structuring and storing text from PDFs.**

This package emerges as the solution to a challenge in which I
had to obtain and store clinical data but can be used for any other purpose.

Package installation
====================

Download and install this package.
To install this package you should run:

.. code-block:: bash

  python3 setup.py install


Extracting PDF Text
===================

PDF TOOLBOX it is designed to read PDFs from multiple sources.

The `pdf.readers.filereader` module implements the reading of PDFs stored as files.
To read PDFs stored in memory, in a rabbitmq or in another data source,
it is necessary to create your own implementation that respects the
interface defined in `pdf.domain.pdfreader`.

**Example usage**

Retrieving text from a PDF file:

.. code-block:: python

  from pdf_toolbox.pdf.readers.filereader import FilePDFReader

  pdf_reader = FilePDFReader("inputs/report.pdf")

  pdf_text = pdf_reader.extract_text()


Parsing PDF Text
----------------

PDF text can have as parsers as PDF types are in the world.

The provided parser parses the PDF text of the challenge.
The provided parser obtains the text of a specific clinical
PDF and returns its information structured in a dictionary.

**Example usage**

.. code-block:: python

  from pdf_toolbox.text_extraction.report_parsers.challenge_parser import ChallengeParser

  challenge_parser = ChallengeParser(pdf_text)
  pdf_data = challenge_parser.parse()


You can define your own parser for other PDF types by implementing the
`ReportParser` interface located in `text_extraction.domain.report_parser`.

Storing PDF parsed data
=======================

Creating an identifier for the report
-------------------------------------

Before saving the report data we should have defined an identifier for it. This package has a shortcut for it.

The method `create_id` returns a new uuid version 4 identifier.

**Example usage**

.. code-block:: python

  from pdf_toolbox.shared.utils import create_id

  report_id = create_id()


Saving report data
------------------

The use of a JSON file as a storage backend is implemented in this package. 

**Example usage**

.. code-block:: python

  from pdf_toolbox.report_storage.storages.json_storage import JSONStorage

  json_storage = JSONStorage("demo.json")
  json_storage.save(pdf_data, report_id)

Any type of backend can be implemented without losing compatibility with the rest of the code. Every storage backend must implement the interface `report_storage.domain.storage.Storage`.

Running tests
=============

To run the tests of this package you must install dev_requirements.txt and
run pytest inside pdf_toolbox folder.

.. code-block:: bash
  pip install -r dev_requirements.txt
  cd pdf_toolbox
  pytest

LICENSE MIT
===========

Copyright 2022 Samuel López Saura

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
