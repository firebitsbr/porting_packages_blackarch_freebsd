PORTNAME=	libosmocore
DISTVERSION=	1.10.0.r47.g38eb428
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Collection of common code used in various sub-projects inside the Osmocom family of projects.
WWW=		https://osmocom.org/projects/libosmocore/wiki/Libosmocore

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/libmnl \
		??/liburing \
		??/libusb \
		??/lksctp-tools \
		??/pcsclite \
		??/talloc \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
