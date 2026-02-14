PORTNAME=	metaforge
DISTVERSION=	115.7b32693
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Auto Scanning to SSL Vulnerability.
WWW=		https://github.com/chriswmorris/Metaforge

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/perl-image-exiftool \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dominate@${PY_FLAVOR} \
		??/py-progress@${PY_FLAVOR} \
		??/py-pyexifinfo@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
