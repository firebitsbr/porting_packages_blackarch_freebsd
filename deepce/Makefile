PORTNAME=	deepce
DISTVERSION=	126.420b1d1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Docker Enumeration, Escalation of Privileges and Container Escapes.
WWW=		https://github.com/stealthcopter/deepce

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bind \
		??/docker \
		??/jq \
		??/kubectl \
		??/lxc \
		??/podman \
		ftp/curl \
		ftp/wget \
		lang/python \
		security/nmap \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
