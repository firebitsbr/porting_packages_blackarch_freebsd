PORTNAME=	ssh-honeypot
DISTVERSION=	113.4bda71c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fake sshd that logs ip addresses, usernames, and passwords.
WWW=		https://github.com/droberson/ssh-honeypot

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/clang \
		??/json-c \
		??/make \
		devel/git

RUN_DEPENDS=	??/libssh \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
