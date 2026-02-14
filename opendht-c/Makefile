PORTNAME=	opendht-c
DISTVERSION=	v3.7.0rc8.r8.g1abaddba
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	C++17 Distributed Hash Table implementation.
WWW=		https://github.com/savoirfairelinux/opendht

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/cython \
		??/fmt \
		??/http-parser \
		??/msgpack-cxx \
		??/restinio \
		??/samurai \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python

RUN_DEPENDS=	??/argon2 \
		??/asio \
		??/gnutls \
		??/jsoncpp \
		??/nettle \
		??/readline


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
