"""Base class for HTML formatters.

This object encapsulates the rendering of various objects to HTML.
You may, and should, derive and override from this object in order to
provide links within a web interface.
"""
from beancount.parser import printer


class HTMLFormatter:
    """A trivial formatter object that can be used to format strings as themselves.
    This mainly defines an interface to implement.
    """

    def render_account(self, account_name):
        """Render an account name.

        Args:
          account_name: A string, the name of the account to render.
        Returns:
          A string of HTML to be spliced inside an HTML template.
        """
        return account_name

    def render_link(self, link):
        """Render a link.

        Args:
          link: A string, the name of the link to render.
        Returns:
          A string of HTML to be spliced inside an HTML template.
        """
        return link

    def render_doc(self, filename):
        """Render a document path.

        Args:
          filename: A string, the filename for the document.
        Returns:
          A string of HTML to be spliced inside an HTML template.
        """
        return filename

    def render_event_type(self, event):
        """Render an event type.

        Args:
          event: A string, the name of the even type.
        Returns:
          A string of HTML to be spliced inside an HTML template.
        """
        return event

    def render_commodity(self, base_quote):
        """Render a commodity (base currency / quote currency).

        This is only used when we want the commodity to link to its prices.

        Args:
          commodity: A pair of strings, the base and quote currency names.
        Returns:
          A string of HTML to be spliced inside an HTML template.
        """
        return '{} / {}'.format(*base_quote)

    def render_source(self, source):
        """Render a reference to the source file.

        Args:
          source: A Source object.
        Returns:
          A string of HTML to be spliced inside an HTML template.
        """
        return printer.render_source(source)