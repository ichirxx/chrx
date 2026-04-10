"""Response models for the EvilMail SDK."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


# ---------------------------------------------------------------------------
# Temp Email
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TempEmail:
    """A newly created temporary email address."""

    email: str
    domain: str
    session_token: str
    ttl_minutes: int
    expires_at: str


@dataclass(frozen=True)
class InboxMessage:
    """Summary of a single message in an inbox listing."""

    uid: int
    sender: str
    subject: str
    date: str
    seen: bool


@dataclass(frozen=True)
class TempInbox:
    """Inbox contents for a temporary email address."""

    messages: List[InboxMessage] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Accounts
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Account:
    """An email account."""

    email: str
    domain: str
    created_at: str


@dataclass(frozen=True)
class CreatedAccount:
    """Result of creating an email account."""

    email: str


@dataclass(frozen=True)
class DeleteResult:
    """Result of a bulk-delete operation."""

    deleted_count: int


# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Message:
    """Full email message with body content."""

    uid: int
    sender: str
    subject: str
    text: Optional[str]
    html: Optional[str]
    date: str
    seen: bool


# ---------------------------------------------------------------------------
# Verification Codes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class VerificationCode:
    """An extracted verification code from a service email."""

    code: str
    service: str
    email: str
    sender: str
    subject: str
    date: str


# ---------------------------------------------------------------------------
# Random Email
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RandomEmailPreview:
    """Preview of a randomly generated email address (not yet created)."""

    username: str
    email: str
    password: str
    domain: str = ""


@dataclass(frozen=True)
class RandomEmailEntry:
    """A single entry in a batch-created random email result."""

    email: str
    password: str


@dataclass(frozen=True)
class RandomEmailBatch:
    """Result of batch-creating random email addresses."""

    count: int
    emails: List[RandomEmailEntry] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Domains
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Domains:
    """Available email domains grouped by type."""

    free: List[str] = field(default_factory=list)
    premium: List[str] = field(default_factory=list)
    customer: List[str] = field(default_factory=list)
    package_type: Optional[str] = None
    authenticated: bool = False
