PORTNAME=	cvechecker
DISTVERSION=	4.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The goal of cvechecker is to report about possible vulnerabilities on your system, by scanning the installed software and matching the results with the CVE database.
WWW=		https://github.com/sjvermeu/cvechecker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/autoconf \
		??/automake \
		??/libbsd

RUN_DEPENDS=	??/libbsd \
		??/libconfig \
		??/sqlite3 \
		ftp/wget \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
